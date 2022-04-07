#!/bin/bash

# Start the Session Generator server in Prod

echo 'Starting Session Generator server...'
export FLASK_APP=session_generator.py
flask run -h localhost -p 5003
