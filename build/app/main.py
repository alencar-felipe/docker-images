import docker

def main():
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')

    client.images.build(path="/docker-images/my-latex")

if __name__ == '__main__':
    main()