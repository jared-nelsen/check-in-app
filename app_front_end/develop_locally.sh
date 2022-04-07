#!/bin/bash
# Develop the App Front End Locally

echo 'App Front End starting...'
fuser -k 5555/tcp
gnome-terminal -e 'sh -c "echo ''App Front End console...''; flutter build web; flutter run -d chrome --web-port 5555"'