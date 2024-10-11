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
name: {job_name}
runs-on: ubuntu-latest
env:
  DOCKERHUB_USERNAME: ${{{{ vars.DOCKERHUB_USERNAME }}}}

steps:
  - name: Checkout code
    uses: actions/checkout@v4

  - name: Set up Buildx
    uses: docker/setup-buildx-action@v3

  - name: Log in to Docker Hub
    uses: docker/login-action@v3
    with:
      username: ${{{{ vars.DOCKERHUB_USERNAME }}}}
      password: ${{{{ secrets.DOCKERHUB_PASSWORD }}}}

  - name: Build and push image
    run: docker buildx build --push {args}

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

  latest: str = index.get("latest")
  tags: dict[str, dict[str, str]] = index.get("tags") or {"latest": {}}
  needs: list[str] = index.get("needs") or []

  jobs = {}
  for tag, build_args in tags.items():

    job_name = get_job_name(image_name, tag)

    args = f"-t ${{DOCKERHUB_USERNAME}}/{image_name}:{tag} "
    if tag == latest:
      args += f"-t ${{DOCKERHUB_USERNAME}}/{image_name}:latest "
    for key, value in build_args.items():
      args += f"--build-arg {key}=\"{value}\" "
    args += f"{str(image_path.relative_to(ROOT_PATH))} "

    job = yaml.safe_load(JOB_TEMPLATE.format(job_name=job_name, args=args))

    if needs:
      job["needs"] = [get_job_name(need) for need in needs]

    jobs[job_name] = job

  return jobs


def get_job_name(image_name, tag="latest"):
  if ":" not in image_name:
    image_name = f"{image_name}:{tag}"
  for c in ":.":
    image_name = image_name.replace(c, "-")
  return image_name

if __name__ == "__main__":
    main()