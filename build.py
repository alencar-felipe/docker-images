#!/usr/bin/env python3
from pathlib import Path
from typing import Optional
import yaml
import subprocess
import sys

ROOT_PATH = Path(__file__).parent

def build(
    image_name,
    tag: Optional[str] = None,
    user: Optional[str] = None
):
    tag = tag or "latest"
    user = user or "alencarfelipe"

    image_path = ROOT_PATH / image_name
    index_path = image_path / "index.yaml"

    if not image_path.exists():
        raise FileNotFoundError(f"Image {image_name} not found.")

    index = {}
    if index_path.exists():
        with open(index_path, "r") as file:
            index = yaml.safe_load(file)

    tags: dict[str] = index.get("tags") or {"latest": []}
    build_args = tags.get(tag) or {}

    full_tag = image_name
    if tag:
        full_tag = f"{full_tag}:{tag}"
    if user:
        full_tag = f"{user}/{full_tag}"

    cmd = ["docker", "build", "-t", full_tag]
    for key, value in build_args.items():
        cmd += ["--build-arg", f"{key}={value}"]

    cmd.append(str(image_path))
    subprocess.run(cmd, check=True)

def parse_arg(text: str):
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
    if len(sys.argv) < 2:
        print("Usage: build_image.py [<user>/]<image_name>[:<tag>]")
        sys.exit(1)

    build(*parse_arg(sys.argv[1]))
