PROJECT = 20200530-quiz
ID = pikesley/${PROJECT}

all: build

build:
	docker build \
		--tag ${ID} .

run:
	docker run \
		--name ${PROJECT} \
		--volume $(shell pwd)/${PROJECT}:/opt/${PROJECT} \
		--publish 8000:8000 \
		--interactive \
		--tty \
		--rm \
		${ID} \
		bash

