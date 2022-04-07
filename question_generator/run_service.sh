#!/bin/bash

# Start the Question Generator server in Prod

echo 'Starting Generator server...'
export FLASK_APP=question_generator.py
flask run -h localhost -p 5004
