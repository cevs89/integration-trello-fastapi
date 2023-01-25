# SpaceX Challenge
This Challenge is about publishes cards in Trello from the API

## Python Version
`3.8`

## API Execute
See the Documentation: `app/README.md`

## Comments
In this project I recommende make a log for every requests we make foy out logs for any error, Also is very important we make Authentication and Authorization for our endpoint.

In this case I don't make this, i want to show you my skill in development and package python way, but i never make a API without Auth and I always using a Database.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the project.

## Docker install and Run
> You need to install docker and docker-compose for this step

### We need declare the follows env:
> It's very important did this step, if you don't declared this env the projects won't work.
The key and token that you need you can find in trello.

* `KEY_AUTH=YOUR_KEY_AUTH`
* `TOKEN_AUTH=YOUR_TOKEN_AUTH`

### Build and RUN
* Build docker: `docker-compose build`
* Run project from Docker: `docker-compose up`

#### or
After the build:

* Run project from Docker: `docker-compose up -d`
* Check the logs: `docker-compose logs -f`

## Install this if you need to development
> or if you wanna run the project with virtualenv and the command uvicorn from server

## Install Base dependency
`pip install -r requirements/base.txt`

### How to set up dev tools
* install dev requirements  `pip install -r requirements/dev.txt`
* run  `pre-commit install`

### How to set up linters tools
* install linters requirements  `pip install -r requirements/linters.txt`

### How to run linters?
There are 3 types of linters:
* Black: Which formats the python code to black style: `black app/`
* Flake8: which analyze code: `flake8 app/`
* Isort: isort your imports, so you don't have to: `isort app/ --profile black`

### You can also run all linters as follows:

* `pre-commit run --all-files`

Source: https://share-docs.clickup.com/p/h/e12h-16043/f3e54f9ffd37f57
