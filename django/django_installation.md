# Installation

1.Installing Python 3.6.2
- sudo apt-get update
- sudo apt-get install python3.6

2.Installing Virtualenv

Below steps are to install pip for python 3.6
    - wget https://bootstrap.pypa.io/get-pip.py
    - sudo python3.6 get-pip.py
Below steps are to install virtualenv
    - sudo pip3.6 install virtualenv

I am going to create a folder named development for my further projects and in it i am creating project folder to to hold this new project.

3.Creating new folder project
- mkdir project
- cd project

4.Installing virtual environment with python
- virtualenv venv -p python

After running the above command our virtual environment is created. Now before we start using it, we need to activate:
- source venv/bin/activate

5.Installing Django 1.11.4
- pip install django

6.Starting a New Project
- django-admin startproject project
- python manage.py runserver

7.Go to the directory where the manage.py file is and executes the following command:
- django-admin startapp first

8.Add our first project to installed apps in settings.py
9.Add following code to view.py in first app.
{
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World!')
}

10.Now we have to tell Django when to serve this view. It’s done inside the urls.py file:
{
from django.conf.urls import url
from django.contrib import admin

from first import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
]
}

11. Finally run the server.
- python manage.py runserver












