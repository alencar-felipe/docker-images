ROOT_DIR = $(abspath .)
IMAGE_NAME = $(shell basename $(ROOT_DIR))
HUB_USER = alencarfelipe

latest:
	docker build $(ROOT_DIR) \
	-t $(HUB_USER)/$(IMAGE_NAME):$@ \

	docker push $(HUB_USER)/$(IMAGE_NAME):$@ 

all: latest