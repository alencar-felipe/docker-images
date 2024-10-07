#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT_PATH = Path(__file__).parent

WORKFLOW_TEMPLATE = """
name: build

"on":
  push:
    branches:
      - main

  schedule:
    - cron: "0 0 1 * *"

"""

JOB_TEMPLATE = """
name: {image_name}
runs-on: ubuntu-latest
env:
  DOCKERHUB_USERNAME: ${{{{ vars.DOCKERHUB_USERNAME }}}}

steps:
  - name: Checkout code
    uses: actions/checkout@v3

  - name: Set up Buildx
    uses: docker/setup-buildx-action@v2

  - name: Cache Docker layers
    uses: actions/cache@v3
    with:
      path: /tmp/.buildx-cache
      key: ${{{{ runner.os }}}}-buildx-${{{{ github.sha }}}}
      restore-keys: ${{{{ runner.os }}}}-buildx-

  - name: Log in to Docker Hub
    uses: docker/login-action@v2
    with:
      username: ${{{{ vars.DOCKERHUB_USERNAME }}}}
      password: ${{{{ secrets.DOCKERHUB_PASSWORD }}}}

  - name: Build and push image
    run: |
        GIT_HASH=$(git rev-parse --short HEAD)
        docker buildx build \
          --cache-from type=local,src=/tmp/.buildx-cache \
          --cache-to type=local,dest=/tmp/.buildx-cache \
          --push \
          -t ${{DOCKERHUB_USERNAME}}/{image_name}:{image_tag} \
          -t ${{DOCKERHUB_USERNAME}}/{image_name}:${{GIT_HASH}}-{image_tag} \
          ./{image_name}

"""


def main():
  index_path = ROOT_PATH / "index.yaml"
  workflow_path = ROOT_PATH / ".github" / "workflows" / "build.yaml"

  with open(index_path, "r") as file:
    manifest = yaml.safe_load(file)

  jobs = {}
  for image_name in manifest["images"]:
    jobs.update(image_jobs(image_name))

  workflow = yaml.safe_load(WORKFLOW_TEMPLATE)
  workflow["jobs"] = jobs

  with open(workflow_path, "w") as file:
    yaml.safe_dump(workflow, file, sort_keys=False)


def image_jobs(image_name: str) -> dict:
  image_path = ROOT_PATH / image_name
  index_path = image_path / "index.yaml"

  if not image_path.exists():
    raise FileNotFoundError(f"Image {image_name} not found.")

  index = {}
  if index_path.exists():
    with open(index_path, "r") as file:
      index = yaml.safe_load(file)

  tags: dict = index.get("tags", {"latest": []})
  needs: list = index.get("needs", [])

  jobs = {}
  for tag, args in tags.items():

    job = yaml.safe_load(JOB_TEMPLATE.format(
      image_name=image_name,
      image_tag=tag,
      args=args_fmt(args)
    ))

    if needs:
      job["needs"] = needs.copy()

    jobs[image_name] = job

  return jobs


def args_fmt(args: dict) -> str:
  if not args:
    return ""

  return "".join(
      f"--build_arg {key}=\"{value}\" "
      for key, value in args.items()
  )


if __name__ == "__main__":
    main()