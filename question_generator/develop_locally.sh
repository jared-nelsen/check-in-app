#!/bin/bash

# Develop Question Generator Locally

echo 'Starting Question Generator server...'
fuser -k 5004/tcp
gnome-terminal -e 'sh -c "echo ''Question Generator server...''; . venv/bin/activate; export FLASK_APP=question_generator.py; flask run -h localhost -p 5004;"'