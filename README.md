# Django on Docker
This project provides a template for running Django applications in Docker containers using docker-compose.

# Overview
The project consists of:

A Django app in src/
Dockerfile to build Django image
docker-compose.yml to run Django, PostgreSQL, and other services
README with instructions
The Django app is baked into its own Docker image. PostgreSQL runs in a separate container.

# Quickstart
To get started:

Clone this repo

Build the images:

docker-compose build



# Start the containers:

docker-compose up



The app will be available at http://localhost:8000 by default.

An admin user is automatically created with username admin and password password.

# Django App
The Django project is under src/. It contains:

settings.py - Django settings configured for Docker. Database, staticfiles, allowed hosts, etc are all setup.
wsgi.py - WSGI app config.
urls.py - Main URL routes.
The src/ directory is added to the image as a volume so you can edit locally and changes will apply.

# Docker Images
The docker-compose.yml file defines two images:

web - The Django app. Build from Dockerfile.
db - The PostgreSQL database. Uses official PostgreSQL image.
Docker Compose
The Docker containers are defined in docker-compose.yml.

To start the containers:

docker-compose up



To rebuild images and restart containers:

docker-compose up --build



Django migrations will be applied automatically on container start.

Static files are collected automatically too.

# Container Commands
You can execute commands in the running containers with docker-compose exec:

# Django shell
docker-compose exec web python manage.py shell

# Database shell
docker-compose exec db psql --username=hello_django --dbname=hello_django

# New migration
docker-compose exec web python manage.py makemigrations

# Collect static
docker-compose exec web python manage.py collectstatic



#Deployment
The containers can be deployed as-is to any Docker host.

For production, you should:

Configure Django settings for production
Enable Django's SECRET_KEY env variable
Set the DEBUG env variable to False
