# Django-Basic-Project

## Creating a Virtual Environment

Start by creating a project folder and making a virtual environment

```
mkdir Django-Demo
cd Django-Demo

# To install virtualenv
pip install virtualenv

# Creating a virtualenv
virtualenv env
env\Scripts\activate    # For Windows Users
```

## Initialize your Django Project

Make Django Project and initial Django app inside your project

```
# Install Django on virtual environment
pip install django
pip install djangorestframework

# Start Django Project
django-admin startproject Demo
cd Demo
django-admin startapp app

# Making Initial migrations
python manage.py migrate

# Creating Superuser
python manage.py createsuperuser
```

## Run your Django Project

In order to run your Django Server use the following command

```
python manage.py runserver
```

## Migrate your models

After creating models make sure you migrate them to the database by using the following commands

```
python manage.py makemigrations
python manage.py migrate
```