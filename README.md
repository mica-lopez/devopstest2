1 : Create the DockerFile to build the Django application container
===========================================
* install dependencies (requirements.txt)
* run migrate everytime the container starts
* use uwsgi to run the application in http mode

2: Run the container using docker-compose on each EC2 instances
===========================================
On one of the EC2 instances, the docker-compose stack will include MySQL 5.7 and will have the DB server role. Each EC2 will run the web application.

* create docker-compose.yml
* modify the application to get the DB credentials from ENV instead of hardcoded
* Inject the necessary DB information and credentials to connect to the DB
