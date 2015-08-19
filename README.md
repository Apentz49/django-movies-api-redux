# Django Movie API

## Description

Create a RESTful API using Django Rest Framework to add update and delete a movie. 

## Learning Objectives

After completing this assignment, you should be able to:

* Create an API on a basic model using Django Rest Framework
* Use token authentication

## Details

### Deliverables

* A Git repo called django-movies-api containing at least:
  * a `requirements.txt` file
  * a `README.md` file
  * a Django project called `crud` containing an app with API views for the Movie model.

### Normal Mode

Included is a basic app where template driven views allow a user to create/read/delete new and existing
movies in the database.  Create an app called `api` that all API requests will use and correctly perform the `verb` you are expecting.

Required verbs to implement:
 - GET
 - POST
 - PUT
 - DELETE

Required functionality to implment:
 - Query for all movies
 - Query for a specific movie
 - Create a new movie in the database
 - Update existing fields on an existing movie
 - Delete an existing movie
 - Secure endpoints to the owner or a superuser
 - Use both basic and token authentication schemes
 - Create tests to test the endpoints

You must use Django Rest Framework for this homework. How you do this is up to you as the framework is large.  

### Hard Mode

In addition to `normal mode` add a rating system.  The new ratings should be able to be managed through the api. Additionally, they should be able to be attached to the movie.

### Additional Resources:

[Naming RESTful resources](http://www.restapitutorial.com/lessons/restfulresourcenaming.html)

[Django Rest Framework Tutorial](http://www.django-rest-framework.org/#tutorial)
