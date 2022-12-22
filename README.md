# recommendation-system-with-azure
Project 9 : A recommendation system with azure cloud


# Overview
This repository contains a flask API that handles requests to an azure function connected to a cosmosDB azure database which has been initially
loaded from the results of our svd recommendation system (on premise).
The database contains a description of users and a list of the recommended articles for each user



# the flask API
The 'Flask application' folder contains the code of the flask API : 'app.py' developped in python 
To run the API locally, use the following :
```
flask run
```
We  enter a userID and the API shows the recommended articles. The API requests the azure function :azure-func11 (see app folder) 
which get data using a binding to cosmosDB.
To access the Flask API locally :
```
http://127.0.0.1:5000/
```


# Azure Function

The 'app' folder contains the code of the azure function developped with vscode
for unit testing the azure function for the userID=30, use the following :
```
https://azure-func-11.azurewebsites.net/api/azure-func11?userId=30
```


