ROOT_DIR = $(abspath .)
IMAGE_NAME = $(shell basename $(ROOT_DIR))
HUB_USER = alencarfelipe

latest:
	docker tag \
	$(HUB_USER)/$(IMAGE_NAME):10.3-2021.10-bullseye-slim \
	$(HUB_USER)/$(IMAGE_NAME):$@

	docker push $(HUB_USER)/$(IMAGE_NAME):$@

10.3-2021.10-bullseye-slim:
	docker build $(ROOT_DIR) \
	-t $(HUB_USER)/$(IMAGE_NAME):$@ \
	--build-arg BASE_IMAGE=debian:bullseye-slim \
	--build-arg GNU_RM_VER=10.3-2021.10

	docker push $(HUB_USER)/$(IMAGE_NAME):$@

all: 10.3-2021.10-bullseye-slim latest