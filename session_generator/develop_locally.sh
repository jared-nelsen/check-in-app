#!/bin/bash

# Develop Session Generator Locally

echo 'Starting Session Generator server...'
fuser -k 5003/tcp
gnome-terminal -e 'sh -c "echo ''Session Generator server...''; . venv/bin/activate; export FLASK_APP=session_generator.py; flask run -h localhost -p 5003;"'