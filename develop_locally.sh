#!/bin/bash

# Starts the local development environment

# Start local Firebase
cd firebase
sh ./start_firebase_emulator.sh
cd ..

# Start the Notification Generator
cd notification_generator
sh ./develop_locally.sh
cd ..

# Start the Landing Page Back End
cd ui_back_end
sh ./develop_locally.sh
cd ..

# Start the Session Generator
cd session_generator
sh ./develop_locally.sh
cd ..

# Start the Question Generator
cd question_generator
sh ./develop_locally.sh
cd ..

cd heartbeat_service
sh ./develop_locally.sh
cd ..

# Start the App Front End
cd app_front_end
sh ./develop_locally.sh
cd ..