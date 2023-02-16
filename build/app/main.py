import os
import docker
import yaml

from pathlib import Path

def main():

    PUSH_EN = getenv('PUSH_EN', False, bool)
    HUB_USER = getenv('HUB_USER', 'alencarfelipe', str)
    HUB_PASS = getenv('HUB_PASS', None, str)
    DOCKER_URL = getenv('DOCKER_URL', 'unix://var/run/docker.sock', str)
    IMAGES_PATH = getenv('IMAGES_PATH', '/docker-images', Path)

    BUILD_YAML = IMAGES_PATH / 'build.yaml'
    IMAGE_YAML = 'image.yaml'

    client = docker.DockerClient(base_url=DOCKER_URL)
    
    if HUB_USER is not None and HUB_PASS is not None:
        client.login(username=HUB_USER, password=HUB_PASS)

    build_conf = load_yaml(BUILD_YAML)
    
    failed = False

    for image_name in build_conf['images']:
        image_conf = load_yaml(IMAGES_PATH / image_name / IMAGE_YAML)
        
        for tag, args in image_conf['tags'].items():
            repository = f'{HUB_USER}/{image_name}'
            complete = f'{repository}:{tag}'
            
            print(f'{complete} ... ', end='', flush=True)

            try :
                client.images.build(
                    path=str(IMAGES_PATH / image_name),
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

def getenv(key, default, type_):
    res = os.getenv(key, default=default)

    if res is not None:
        res = type_(res)

    return res

if __name__ == '__main__':
    main()