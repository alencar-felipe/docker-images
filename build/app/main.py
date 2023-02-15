import os
import docker
import yaml

from pathlib import Path

PUSH_EN = bool(os.environ['PUSH_EN'])
HUB_USER = os.environ['HUB_USER']
HUB_PASS = os.environ['HUB_PASS']
DOCKER_URL = 'unix://var/run/docker.sock'
IMAGES = Path('/__w/docker-images/docker-images')
BUILD_YAML = IMAGES / 'build.yaml'
IMAGE_YAML = 'image.yaml'

def main():
    client = docker.DockerClient(base_url=DOCKER_URL)
    client.login(username=HUB_USER, password=HUB_PASS)

    build_conf = load_yaml(BUILD_YAML)
    
    failed = False

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
                failed = True
                continue
            
            if PUSH_EN:
                try:   
                    resp = client.api.push(
                        repository=repository,
                        tag=tag,
                        stream=True,
                        decode=True    
                    )

                    for line in resp:
                        if 'errorDetail' in line:
                            raise Exception(str(line))

                except:
                    print('Push Error')
                    failed = True
                    continue

            print('Ok')

    if failed :
        exit(-1)

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

if __name__ == '__main__':
    main()