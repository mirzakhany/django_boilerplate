#!/bin/sh

DOCKER_FILE="deploy/BaseDockerfile"
BASE_URL="https://$DOCKER_REGISTRY/v1/"

REQ_HASH=$(cat requirements.txt $DOCKER_FILE | md5sum | awk '{print $1}')

echo "check docker registry for image tag: $BASE_IMAGE_REPO:$REQ_HASH"
IMAGE=$(curl -s -u $DOCKER_USER:"$DOCKER_PASS" -X GET $BASE_URL/$BASE_IMAGE_REPO/tags/list | grep $REQ_HASH)

if [ ! $IMAGE ]; then
    echo "Base image for base not exists, now building ..."
    docker build \
        -f $DOCKER_FILE \
        -t $BASE_IMAGE_REPO:$REQ_HASH \
        --build-arg BUILD_DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
        --build-arg VCS_REF="$REQ_HASH" \
    

    if [ $? -ne 0 ]; then
        echo "error in build process"
        exit 1
    fi

    docker login -u $DOCKER_USER -p "$DOCKER_PASS" $DOCKER_REGISTRY
    docker push $BASE_IMAGE_REPO:$REQ_HASH
else
    echo "Base image for base already exists"
fi
