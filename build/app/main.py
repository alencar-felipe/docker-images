import docker
import yaml

from pathlib import Path

HUB_USER = 'alencarfelipe'
DOCKER_URL = 'unix://var/run/docker.sock'
ROOT = Path('/')
IMAGES = ROOT / 'docker-images'
BUILD_YAML = IMAGES / 'build.yaml'
IMAGE_YAML = 'image.yaml'

def main():
    client = docker.DockerClient(base_url=DOCKER_URL)

    build_conf = load_yaml(BUILD_YAML)
    
    for image_name in build_conf['images']:
        image_conf = load_yaml(IMAGES / image_name / IMAGE_YAML)
        
        for tag, args in image_conf['tags'].items():
            repository = f'{HUB_USER}/{image_name}'
            complete = f'{repository}:{tag}'
            
            print(f'{complete} ... ', end='', flush=True)

            try :
                client.images.build(
                    path=str(IMAGES / image_name),
                    tag=complete,
                    rm=True,
                    buildargs=args
                )
            except:
                print('Build Error')
                continue
            
            try:
                client.images.push(
                    repository=repository,
                    tag=tag    
                )
            except:
                print('Push Error')
                continue

            print('Ok')

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

if __name__ == '__main__':
    main()