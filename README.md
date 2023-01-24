# SpaceX Challenge
This Challenge is about publishes cards in Trello from the API

## Python Version
`3.8`

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the project.

## Install this if you need to development

### How to set up dev tools
* install dev requirements  `pip install -r requirements/dev.txt`
* run  `pre-commit install`

### How to set up linters tools
* install linters requirements  `pip install -r requirements/linters.txt`

### How to run linters?
There are 4 types of linters:
* Black: Which formats the python code to black style: `black app/`
* Flake8: which analyze code: `flake8 app/`
* Isort: isort your imports, so you don't have to: `isort app/ --profile black`
* Safety: Safety packages: `safety check -r requirements/file_name.txt`

### You can also run all linters as follows:

`pre-commit run --all-files`
