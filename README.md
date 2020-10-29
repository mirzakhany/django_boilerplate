# Django Boilerplate

This project is going to be a template for starting django projects. and will cover:

* [ ] Clean project structure
* [ ] Auth setup and drf with jwt
* [ ] Dockerfiles
* [ ] Setup and deployment of celery task manager
* [ ] CI/CD
* [ ] Kubernetes deployment with helm and docker compose file
* [ ] ?


# Setup project
### Install dependencies
Install development environment packages and dependencies:
```
pip install -r requirements/requirements-dev.txt
```

### Install pre-commit git hook
```
pre-commit install
```

### Load configs using `env` file
Copy `.sample_env` file into `.env` and update the values.

### How to generate requirements-dev.txt file with pip-compile
```
pip-compile --output-file=requirements/requirements-base.txt requirements/requirements-base.in
pip-compile --output-file=requirements/requirements-base.txt requirements/requirements-dev.in
```

### How to build docker images.

We have two scripts in `deploy/scripts` directory to make build process easier in CI/CD. but we can also use them during development.

### First of all set required variables
There is a file called `values_sample.sh` in `deploy/scripts`. rename this file and make sure to add it to `.gitignore`.

This file content is:

```bash
export DOCKER_REGISTRY="index.docker.io";
export DOCKER_USER="";
export DOCKER_PASS="";

export BASE_IMAGE_REPO="mirzakhani/django_boilerplate_base";
export IMAGE_REPO="mirzakhani/django_boilerplate";
```

`DOCKER_REGISTRY`: is to set your docker register address, default address will work for dockerhub.

`DOCKER_USER` and `DOCKER_PASS` are used to login to your docker registry. !!! Again don't forget to put this file in `.gitignore` !!!

`BASE_IMAGE_REPO` and `IMAGE_REPO` are your images repositories. [but why two docker image?](#why-two-docker-image)

#### Build images

First load settings.
```bash
source ./deploy/scripts/.values.sh
```

Then build base image.
```bash
./deploy/scripts/build_base_image.sh
```

And finaly build project docker image:
```bash
./deploy/scripts/build_image.sh
```

##### Why two docker image

If you check `deploy` folder you will find a docker file named `BaseDockerfile`. in this docker file we will install our project requirements. so we will not need to install them every time we make final project docker image, and this will save alots of time for use in delivery our code to live environment.
