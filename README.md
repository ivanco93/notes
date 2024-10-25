# AngesGT notes project

<!-- TABLE OF HEADER -->
[![Java][skill-python-shield]][skill-python-url]
[![Django][skill-django-shield]][skill-django-url]

<!-- ABOUT THE PROJECT -->

## About The Project

AndesGT notes is an backend service for CRUD notes and users authentication.

### Project Organization

This section contains the archetype how the project is built and the content of each of the application directories.

    ├── .github
    │   ├── workflows                         
    │   │       └── pipeline.yml              <- github actions pipeline for continuous integration
    ├── notes_project
    │   ├── main                              <- main project owner of settings and route register files
    │   │   ├── __init__.py                   <- required for python packages
    │   │   ├── asgi.py                       <- provides interface for web applications compatible for Asynchronous Server Gateway Interface
    │   │   ├── settings.py                   <- project general configuration
    │   │   ├── urls.py                       <- register of applications general routes
    │   │   └── wsgi.py                       <- provides interface for web applications compatible for Web Server Gateway Interface
    │   ├── notes                             <- Application for notes CRUD           
    │   │   ├── api                           <- contains files related with rest api endpoints for note entity
    │   │   │    ├── __init__.py              <- required for python packages
    │   │   │    ├── router.py                <- declarations of endpoints routes for note entity
    │   │   │    ├── serializers.py           <- serializers used for note endpoints for data treatment
    │   │   │    └── views.py                 <- viewsets with definition of access permissions, main queries, and filters
    │   │   ├── api_tests                     <- contains files related with unit tests for note api files
    │   │   │    ├── __init__.py              <- required for python packages
    │   │   │    ├── test_models.py           <- unit tests for declared models in notes application
    │   │   │    ├── test_routers.py          <- unit tests for declared routers in notes application
    │   │   │    ├── test_serializers.py      <- unit tests for declared serializers in notes application
    │   │   │    └── test_views.py            <- unit tests for declared views in notes application
    │   │   ├──  migrations                   <- folder that locates all migrations files
    │   │   ├── __init__.py                   <- required for python packages
    │   │   ├── admin.py                      <- used for register new views in django-admin panel(not used)
    │   │   ├── apps.py                       <- general configuration of application
    │   │   ├── models.py                     <- declarations of note entities 
    │   │   └── views.py                      <- used for render views in django-admin panel(not used)
    │   ├── users                             <- Application for users CRUD           
    │   │   ├── api                           <- contains files related with rest api endpoints for user entity
    │   │   │    ├── __init__.py              <- required for python packages
    │   │   │    ├── router.py                <- declarations of endpoints routes for user entity
    │   │   │    ├── serializers.py           <- serializers used for user endpoints for data treatment
    │   │   │    └── views.py                 <- viewsets with definition of access permissions, main queries, and filters
    │   │   ├── api_tests                     <- contains files related with unit tests for user api files
    │   │   │    ├── __init__.py              <- required for python packages
    │   │   │    ├── test_models.py           <- unit tests for declared models in users application
    │   │   │    ├── test_routers.py          <- unit tests for declared routers in users application
    │   │   │    ├── test_serializers.py      <- unit tests for declared serializers in users application
    │   │   │    └── test_views.py            <- unit tests for declared views in users application
    │   │   └── migrations                    <- folder that locates all migrations files
    │   │   ├── __init__.py                   <- required for python packages
    │   │   ├── admin.py                      <- used for replacement of User model used for api
    │   │   ├── apps.py                       <- general configuration of application
    │   │   ├── models.py                     <- declarations of user entities 
    │   │   └── views.py                      <- used for render views in django-admin panel(not used)
    │   ├── .coveragerc                       <- coverage tests configuration file 
    │   ├── __init__.py                       <- required for python packages 
    │   ├── createsuperuser.py                <- script used for docker images to create default user 
    │   ├── Dockerfile
    │   ├── manage.py                         <- Script used for Django interactions
    │   ├── nginx.conf                        <- Nginx configuration file used for Docker
    │   └── requirements.txt                  <- Contains all python dependencies 
    ├── .gitignore                            <- Ignored files for Github
    └── README.md                             

<!-- GETTING STARTED -->

## Getting Started

Instructions on how to configure your project locally. To get a working local copy, follow these example steps.

### Prerequisites

* [Python 3.10](https://www.python.org/downloads/)
* [Pycharm](https://www.jetbrains.com/es-es/pycharm/download/) `Recomended`
* [Docker](https://docs.docker.com/engine/install/) `For docker images building and testing`

## Installation


### 💻 Locally

```shell
pip install -r requirements.txt
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```


*Now, you can start the server(defaul port:8000) with the next command
```shell
python manage.py runserver
```
### 🧪 Quality assurance

Run unit tests
```shell
coverage run manage.py test
coverage report
```
<!-- USAGE EXAMPLES -->

## Usage

#### REST APIs

Swagger documentation for [Swagger API](http://localhost:8000/docs)

*Note:* Change the default port(8000) for the used port in deployment


*Service api context Path:*
/docs


# CI/CD

Project uses Github Actions worflows for CI/CD tasks

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://shields.io/ -->

[skill-python-shield]: https://img.shields.io/badge/python-3.10-blue

[skill-python-url]: https://www.python.org/downloads/

[skill-django-shield]: https://img.shields.io/badge/Django%20Rest%20Framework-3.15.2-blue

[skill-django-url]: https://django.io/guides/gs/django-boot/