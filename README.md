Level 1 : Create the Container to run the application
===========================================
* install dependencies (mysql/python3/uwsgi) in the container
* create a virtualenv and install the requirements for python (requirements.txt)
* runs migrate everytime the container starts
* use uwsgi to run the application in http mode

Level 2: Run the container using docker-compose
===========================================
* create docker-compose.yml
* modify the app to get the Database credentials from env
* Inject the necessary DB information and credentials to connect to the db
* Implement an nginx container as a proxy to the application listening on port 80
* retrieve the picture s3://ck-dev-test-yourname/ok.png during application startup
* Configure nginx to serve the images as /static/ok.png on the home page of devopstest application


Level 3 : Run the container using minikube on the EC2 instance
===========================================
* Configure minikube on the EC2 instance
* Create the deployment.yml necessary to run the containers in minikube, connecting to the external RDS
* optional : configure and create the ingress to access the application from the port 80 of the EC2 instance
