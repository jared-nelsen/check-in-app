# Check In App Front End

This project serves as the front end to the Check In App.

# Docker Commands

## Build the container

docker build . -t <container_name>

## Run the container

docker run -i -p 808:4040 -td <container_name>

## Step into the filesystem

docker exec -t -i <container_id> /bin/bash