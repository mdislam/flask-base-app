# Basic Flask app with Nginx proxy and Gunicorn

We use `Makefile` to deploy our simple application and run unit tests inside the docker container

## How to run
`make build-n-deploy`

this command will build the images using docker-compose file and finally will run the containers
in detach mode. See the `docker-compose.yml` file for details.

After successful build and run, open browser and check
`http://localhost/api/v1/app/echo`

this will give a json response like following

`{"version": "1.0.2-alpha", "status": "App is up and running!"}`


## API Documentation
The api documentation could be seen from here: `http://localhost/api/v1/doc`

## Running Unit Test inside docker container
run following command:- 
`make run-unit-tests`        
      