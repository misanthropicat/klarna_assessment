## About

This repo contains package math_app which contains library with implementation of the following math functions:
1. The n:th Fibonacci number
2. The Ackermann function for m and n
3. The factorial n!

As well package contains simple web application with API for using mentioned functions.

## How to start application locally

Application can be started by one of the following ways:

#### Running on host directly

Pre-requirements: python 3.8+, pip
In project root directory execute the following commands:

`pip install -r requirements.txt`
 
`python3 app.py`

#### Running in Docker container

Pre-requirement: docker
In project root directory execute the following command:

`docker-compose up`

In browser navigate to `localhost:8080` to see the swagger.

#### Running in the public cloud

For political reasons beyond my control I'm able only to describe proposal for cloud deployment of this application.
Would be good to check it by creating a PoC.

Proposed using [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.CreateApp.html).

Python or Docker can be used as a platform.