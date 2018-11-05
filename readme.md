# Pingit Clone

This is my personal project to try and emulate the functions of the 'Pingit' app by barclays in the UK. I use Django to make a mock bank with an API which allows transfers, making new accounts, checking balances, etc. This project is me getting back in touch with programming by implementing multiple things such as REST framework and getting to know python and Django better, too.

## Getting Started

If you're interested in trying out the project, check out the steps below. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

I'm working on this project in an Ubuntu/Xenial16.04 LTS. The project runs on python3.6 and I'm currently using virtualenvwrapper for local development. The list of required packages can be seen in the requirements files at requirements/. This project also uses PostgreSQL for the database. So to recap:

1. Python3.6
2. virtualenv
3. Postgresql (>9.5.14) 

### Installing

To get started, simply clone the project to your machine.

```
developer@machine:~/$ git clone https://github.com/HardyHardy08/pingit_clone.git <destination>
```

or

```
developer@machine:~/$ git clone git@github.com:HardyHardy08/pingit_clone.git <destination>
```

and install the requirements

```
developer@machine:~/$ pip install -r pingit_clone/requirements/development.txt 
```

you should be good to go!

To get started and look around the functionalities of the project, run a local django server.

```
developer@machine:~/pingit_clone$ python pingit_clone/manage.py runserver

System check identified no issues (0 silenced).
November 05, 2018 - 12:20:53
Django version 2.1.2, using settings 'pingit_clone.settings.development'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

Go to your browser and enter 127.0.0.1:8000 and you should have a page that says 'You are not logged in'

## Running the tests

I use pytest to run the tests located in pingit_clone/(app)/tests. pytest needs to be run from the django directory (the one with manage.py) to make sure that it can get to test files. 

```
developer@machine:~/pingit_clone/pingit_clone$ pytest
```

This project uses py-cov as a wrapper for pytest and coverage. To get the coverage results run pytest with --cov. The coverage report defaults to the terminal.

```
developer@machine:~/pingit_clone/pingit_clone$ pytest --cov
```

To get the html version of the report, simply run with the --cov-report html option.

```
developer@machine:~/pingit_clone/pingit_clone$ pytest --cov --cov-report html
```
Further options can be seen in the official docs for [Pytest](https://docs.pytest.org/en/latest/), [Tox](https://tox.readthedocs.io), and [Pytest-Cov](https://pytest-cov.readthedocs.io/en/latest/readme.html#).

## Deployment

For how to deploy, refer to this [repo](https://github.com/HardyHardy08/pingit_clone_vagrant_setup). The repo holds files to setup a vagrant that running Ubuntu Xenial; basically a mock server. It's still a WIP, but I'm trying to automate the deployment using plain bash scripts and am testing it out locally for conveniences sake.

## Built With

* [Python3.6](https://docs.python.org/3.6/) - Python docs
* [Django](https://docs.djangoproject.com/en/2.1/) - The web framework used

## Contributing

Everyone is welcome to contribute by making pull requests :) The more 'bank' like this becomes I think the cooler it will be. Will also put up a 'spec sheet' to show what I want the code to be able to do.

## Authors

* **Achmad Hardiansyah**
