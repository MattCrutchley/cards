# Cards microservice web application

## Brief
The objective of this project is to create a web application in python flask developed using mcroservices and for the app to have the capability to swap out services for alternatives with no downtime.

## Project
In order to do this I have decided to create an applicaiton that will create a deck of cards in a sql database, cards can be drawn using another service and  there will also be a service generating a random prize.

## Project tracking 

A trello board was used to track the project, this implemented the use of MoSCoW prioiritisation.


## Services

### Database 
 A container running mysql is first set up with an empty databse and table for the deck initialised inside of it.
 
### Reset
This is a Python service that connects to the SQL database, removes all entries for the deck table and then populatesit  with entries representing a standard deck of cards.

V2 - Version2 of this service populates the database with the cards named in long form i.e "1" becomes "one" and "K" becomes "King"

### Draw 
this is another Python service that, provided the deck is not empty, will connect to the database delete a card from the deck at random and then return its value in JSON format, this service is currently hardcoded to draw two cards however this is set up in for loop so there is scope for it to draw a variable number of cards by accepting a variable containing the nuber of cards to be drawn as the app develops.

### Prize
This service uses python to generate a random number between 1 and 50 and returns it in JSON format.

V2 - Version2 of this service generates a random number between 1 and 50 and returns it in JSON format.

### Frontend 

This service displays a index.html page and has routes that when reached via links on the index.html trigger get requests to the various other services in the case of the draw and prize service the JSON values are then passed to the index.html using flasks render template function, this values can then be displayed on the html pages using Jinja2 syntax.

### nginx

An nginx service is also set up which directs traffic arriving on port 80 to the frontend service, the frontend service then communicates with all other services in the docker compse network removing the need to expose any ports other than 80 on this machine.


## Testing


## Deployment

Jenkins will be used on one VM to run a pipline job, this will run the tests in the application and if they pass, the app will be deployed across two other VM's using docker stack deploy. A webhook will be set up so that if the version number changes on github jenkins will re-reun the tests and redeploy however this time, where applicable the alternative versions of the app will be pulled form docker hub and phased into the deployment with no downtime.

## Risk assesment
