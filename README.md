<div align="center">

  <h1> SIMPLE REST API CAPABLE OF CRUD OPERATION</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/joseph-ademola-570a1974/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>

<sub>Prepared by: <a href="https://www.linkedin.com/in/joseph-ademola-570a1974/" target="_blank">Joseph Ademola</a><br>
<small> September, 2023</small></sub>

</div>


- [Introduction](#introduction)
- [Requirements](#requirements)
- [Setting up the project](#setting-up-the-project)
  - [Create a virtual environment](#create-a-virtual-environment)
  - [Create a new project](#create-a-new-project)
  - [Create a Django app](#create-a-django-app)
- [Dependencies Used](#dependencies-usec)
- [How to use this repository](#how-to-use-this-repo)


---

## Introduction
This documentation is for building a simple REST API capable of CRUD operations on a "person" resource, interfacing with Postgresql database. The API can dynamically handle parameters, such as adding or retrieving a person by name.  Included is an automated testing script that verifies each of the API's operations. 


## Requirements

The following are used for the practice:

1. Windows 10 PC
2. A code editor - VS Code

## Setting up the project
1. Create a virtual environment (env) and activate for the project.
   
```bash
$ C:\stage2\env> scripts/activate
$ cd ..  
```

2. Create a django project
   
```bash
$ C:\stage2\hngx-api> django-admin startproject apiproject
```

3. Create a new Django app

```bash
$ C:\hngx-api\apiproject> django-admin startapp personapi
```

4. Install require packages:
   
```bash
$ pip install djangorestframework
```

5. Add the app, api and rest_framework to INSTALLED APPS in settings.py

```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'rest_framework',
]
```

6. Define the model:
   
```bash
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

```

7. Create a serializers.py file in the app directory:
   
```bash
from rest_framework import serializers
from .models import Person
import re

class PersonSerializer(serializers.ModelSerializer):
     def validate_name(self, value):
        #regex pattern to validate name
        name_pattern = re.compile(r'^[A-Za-z\s]+$') #this accomodate single or double names
        if not name_pattern.match(value):
            raise serializers.ValidationError("Please provide names in letters only")
        return value

     class Meta:
        model = Person
        fields = ['id', 'name']

```

8. Fill the views.py with the following code:

```bash

from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    def get_queryset(self):
        queryset = Person.objects.all()
        name = self.request.query_params.get('name, None')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset
class PersonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

```

9. Project-level urls.py

```bash
"""
URL configuration for apiproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls'))
]

10. App Level Url.py

```bash

from django.urls import path
from api.views import PersonListCreateView, PersonRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', PersonListCreateView.as_view(), name='Get all users or create a user'),
    path('api/<int:pk>/', PersonRetrieveUpdateDestroyView.as_view(), name='Retrieve user,Update user, or delete user'),
]


```
```

## Dependencies Used
pip==23.2.1,  
psycopg2-binary==2.9.5,
gunicorn==20.1.0,
whitenoise==6.5.0,
Django==3.2.21,
djangorestframework == 3.14.0,
python-dotenv == 0.21.1,

asgiref==3.7.2,
bleach==6.0.0,
pytz==2023.3.post1,
six==1.16.0,
sqlparse==0.4.4,
tzdata==2023.3
webencodings==0.5.1


## How to use this Repository
To set up this project on your own system, follow the following instructions:

1.  Clone the repository from GitHub:
   
```bash
$ git clone https://github.com/comrade70/person-api.git
```

2.  Create a build.sh file and put the following code:

```bash
#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
```

3.  Create a requirement.txt file and run this command to install dependencies:
   
```bash
pip install -r requirements.txt
```

4.  Run the database migration
   
```bash
python manage.py makemigrations
python manage.py migrate

```


5.  Launch the development server

```bash
python manage.py runserver 8000
```
This will start the development server at http://127.0.0.1:8000/. Add /api to access the API to perform CRUD OPERATIONS


THANKS FOR READING ! 🎉

