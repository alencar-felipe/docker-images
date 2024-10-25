#!/usr/bin/env python3
import argparse
from pathlib import Path
from pprint import pprint
from typing import Optional
import yaml
import subprocess

DEFAULT_USER = "alencarfelipe"
ROOT_PATH = Path(__file__).parent

def build(
    image_name: str,
    tag: Optional[str] = None,
    user: Optional[str] = None,
    push: bool = True,
    update_cache: bool = True
):
    image_path = ROOT_PATH / image_name
    index_path = image_path / "index.yaml"

    if not image_path.exists():
        raise FileNotFoundError(f"Image {image_name} not found.")

    index = {}
    if index_path.exists():
        with open(index_path, "r") as file:
            index = yaml.safe_load(file)

    latest = index.get("latest") or "latest"
    tag = tag or latest
    tags: dict[str, str] = index.get("tags") or {"latest": []}
    build_args = tags.get(tag) or {}

    user = user or DEFAULT_USER
    full_tag = f"{user}/{image_name}:{tag}"
    cache_tag = f"{user}/{image_name}:cache-{tag}"

    cmd = ["docker", "buildx", "build"]
    if push:
        cmd += ["--push"]

    cmd += ["-t", full_tag]
    if latest != "latest" and latest == tag:
        cmd += ["-t", f"{user}/{image_name}:latest"]

    cmd += [f"--cache-from=type=registry,ref={cache_tag}"]
    if update_cache:
        cmd += [f"--cache-to=type=registry,ref={cache_tag},mode=max"]

    for key, value in build_args.items():
        cmd += ["--build-arg", f"{key}={value}"]

    cmd.append(str(image_path))

    pprint(" ".join(cmd))
    subprocess.run(cmd, check=True)

def parse_arg(text: str):
    if Path(text).is_dir():
        text = Path(text).name

    if "/" in text:
        user, remainder = text.split("/", 1)
    else:
        user = None
        remainder = text

    if ":" in remainder:
        image_name, tag = remainder.split(":")
    else:
        image_name = remainder
        tag = None

    return image_name, tag, user

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Build Docker image with optional push and cache update."
    )
    parser.add_argument(
        "image",
        help="Image name in format [<user>/]<image_name>[:<tag>], or the path"
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Enable pushing to registry."
    )
    parser.add_argument(
        "--update-cache",
        action="store_true",
        help="Enable cache update."
    )

    args = parser.parse_args()
    image_name, tag, user = parse_arg(args.image)

    build(
        image_name,
        tag=tag,
        user=user,
        push=args.push,
        update_cache=args.update_cache
    )