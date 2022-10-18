```
██████╗      ██╗ █████╗ ███╗   ██╗ ██████╗  ██████╗    ███████╗██╗  ██╗
██╔══██╗     ██║██╔══██╗████╗  ██║██╔════╝ ██╔═══██╗   ╚════██║██║  ██║
██║  ██║     ██║███████║██╔██╗ ██║██║  ███╗██║   ██║█████╗ ██╔╝███████║
██║  ██║██   ██║██╔══██║██║╚██╗██║██║   ██║██║   ██║╚════╝██╔╝ ██╔══██║
██████╔╝╚█████╔╝██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝      ██║  ██║  ██║
╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝       ╚═╝  ╚═╝  ╚═╝
                                                                       
```
# Studybud project

## Install
```
cd django-7h
python3 -m venv env
source env/bin/activate
pip3 install requirements.txt
```

## Run
```
cd django-7h/studybud
python3 manage.py runserver
```

### Sequences:
* django project architecture
* setup urls 
* python3 manage.py startapp yourapp
* app installed by set BaseConfig
* create and setup urls
* setup templates directory in project directory
* connect template with views
* split base templates into base and app templates
* pass query parameter and view those by jinja2 template engine
* migrate default database
* create a model
* makemigrations depends on model (Room)
* make django admin from command prompt
* login as admin
* register model (Room) in admin panel
* view models data from views
* make another model Message
* make another model Topic
* migrate database again
* regster in admin panel - Topic and Message
* make create-room form and connect
* create forms from django
* make a function in views for create room
* make another edit views and a url with params
* make confirm delete page
* room delete url
* room delete views
* home topic brows (filter)
* navbar search topic, name, description
* room available