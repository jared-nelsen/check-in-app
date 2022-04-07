#!/bin/bash

# Start the Notification Generator server in Prod

echo 'Starting Notification Generator server...'
export FLASK_APP=notification_generator.py
flask run -h localhost -p 5002
