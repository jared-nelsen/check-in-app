# Heartbeat Service Dockerfile

# Install Dependencies
FROM debian:latest AS build-env
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get clean

# Install Python Dependencies
RUN pip3 install requests Datetime

# Copy the app files
COPY . /usr/local/bin/app
WORKDIR /usr/local/bin/app

# Set the service startup script as executable
RUN ["chmod", "+x", "/usr/local/bin/app/run_service.sh"]

# Start the heartbeat service
ENTRYPOINT ["/usr/local/bin/app/run_service.sh"]