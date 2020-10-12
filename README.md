# Django Boilerplate

this project is going to be a template for starting django projects. and will cover:

* [ ] clean project structure
* [ ] auth setup and drf with jwt
* [ ] dockerfiles
* [ ] setup and deployment of celery task manager
* [ ] ci/cd
* [ ] kubernetes deployment with helm and docker compose file
* [ ] ?


# How to build docker images.
 
We have two scripts in `deploy/scripts` directory to make build process easier in ci/cd. but we can also use them during development.

### First of all set required variables
there is a file called values_sample.sh in `deploy/scripts`. rename this file and make sure to add it to .gitignore.

this file content is: 

```bash
export DOCKER_REGISTRY="index.docker.io";
export DOCKER_USER="";
export DOCKER_PASS="";

export BASE_IMAGE_REPO="mirzakhani/django_boilerplate_base";
export IMAGE_REPO="mirzakhani/django_boilerplate";
```

`DOCKER_REGISTRY`: is to set your docker register address, default address will work for dockerhub.

`DOCKER_USER` and `DOCKER_PASS` are used to login to your docker registry. !!! Again don't forget to put this file in .gitignore !!!

`BASE_IMAGE_REPO` and `IMAGE_REPO` are your images repositories. [but why two docker image?](#Why-two-docke-image)

#### Build images

first load settings.
```bash
source ./deploy/scripts/.values.sh
```

then build base image.
```bash
./deploy/scripts/build_base_image.sh
```

and finaly build project docker image:
```bash
./deploy/scripts/build_image.sh
```

##### Why two docker image

if you check `deploy` folder you will find and docker file named `BaseDockerfile`. in this docker file we will install our project requirements. so we will not need to install them every time we make final project docker image, and this will save alots of time for use in delivery our code to live environment.
