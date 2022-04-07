#!/bin/bash

# Develop Notification Generator Locally

echo 'Starting Notification Generator server...'
fuser -k 5002/tcp
gnome-terminal -e 'sh -c "echo ''Notification Generator server...''; . venv/bin/activate; export FLASK_APP=notification_generator.py; flask run -h localhost -p 5002;"'