# changes_made
1) port number 5001 is exposed in dockerfile, but the same is not updated in app.py file so Made the necessary changes i.e., initialized port no 5001 in app.py app.run(host='0.0.0.0', port=int("5001"))

 2) In the  file "docker-compose.yml", the flask app is running on port number 80 according to flaskapp.conf. But the port number was not in order in the yml file. so changes made accordingly . "8080:80"

 3) Included "restart always" so that the system will not shutdown if the postgresql does not work 

 4) In the yml file,local folder where the data need to be stored is specified incorrectly. "data" -> "./data"
