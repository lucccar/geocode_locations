# Introduction 

This repo is a very simple app for show off purposes. The application was coded with django framework and has a custom management command that feeds a sqlite database with a csv file with some latitude and longitude informations got from google maps API.

The user interface for this project is a basic swagger static from drf_yasg package. It allows to perform requests for both endpoints served by the api.

Although simple, the app is provided with a gunicorn socket and nginx server.

# How to run

## Dependencies

It depends on a few python libraries that are listed in ``` /geocode/requirements.txt```.


## Starting the app

To build and start the app:
``` docker-compose -f docker-compose-deploy.yml up --build ```

This will expose the endpoint: ``` localhost:8080 ``` which is where the swagger web interface can be find.


## The API

This app has 2 routes. 

### /customers/<int:id>/
A get endpoint that receives a id parameter corresponding to the id of the customer one wants to retrieve from the database.

### /customers
A get endpoint retrieves all customers from the database.


## Tests

One can test the application by changing the current directory to the geocode folder and running ``` python manage.py test ```, the django unit test framework will take care of the rest.



