#!/bin/bash

GIT_COMMIT=$(git rev-parse HEAD)
PREVIOUS_GIT_COMMIT=$(git rev-parse HEAD~1)
GIT_COMMIT_SHORT=$(echo $GIT_COMMIT | head -c 8)
LATEST_TAG=$(git describe --abbrev=0 --tags)
IMAGE_TAG=$(echo "$LATEST_TAG.$GIT_COMMIT_SHORT")

REQ_HASH=$(cat requirements.txt deploy/BaseDockerfile | md5sum | awk '{print $1}')
BASE_IMAGE=$(echo "$BASE_IMAGE_REPO:$REQ_HASH")

docker login -u $DOCKER_USER -p $DOCKER_PASS $DOCKER_REGISTRY

docker build \
    -q \
    -f deploy/Dockerfile \
    -t $IMAGE_REPO:$IMAGE_TAG \
    --build-arg IMAGE_TAG="$IMAGE_TAG" \
    --build-arg GIT_COMMIT="$GIT_COMMIT" \
    --build-arg BASE_IMAGE="$BASE_IMAGE" \
    .
