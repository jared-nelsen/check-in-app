#!/bin/bash

# Develop UI Back End locally

echo 'Starting UI Back End server...'
fuser -k 5001/tcp
gnome-terminal -e 'sh -c "echo ''UI Back End server...''; . venv/bin/activate; export FLASK_APP=ui_back_end.py; flask run -h localhost -p 5001;"'