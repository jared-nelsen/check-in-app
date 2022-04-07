#!/bin/bash

# Start the UI Back End server in Prod

echo 'Starting UI Back End server...'
export FLASK_APP=ui_back_end.py
flask run -h localhost -p 5001
