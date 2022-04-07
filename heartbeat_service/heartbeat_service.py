from datetime import datetime, timedelta
import requests

# Endpoints
generate_sessions_endpoint = 'http://localhost:5003/generate-sessions'
generate_notifications_endpoint = 'http://localhost:5002/generate-notifications'

# Parameters
session_generation_time_delta = timedelta(seconds=10)
notification_generation_time_delta = timedelta(seconds=5)

def generateSessions():
    requests.get(generate_sessions_endpoint)
    print("Sessions Generated... - [" + datetime.now().isoformat() + "]")

def generateNotifications():
    requests.get(generate_notifications_endpoint)
    print("Notifications Generated... - [" + datetime.now().isoformat() + "]")

def heartbeat():
    # Record the start time
    start_time = datetime.now()
    # Record the future session generation time
    session_generation_time = start_time + session_generation_time_delta
    # Record thef future notification generation time
    notification_generation_time = start_time + notification_generation_time_delta
    # Forever
    while True:
        # Record the current time
        current_time = datetime.now()
        # Check the session generation time
        if current_time >= session_generation_time:
            # Generate the sessions
            generateSessions()
            # Reset the session generation time
            session_generation_time = current_time + session_generation_time_delta
        # Check the notification generation time
        if current_time >= notification_generation_time:
            # Generate the notifications
            generateNotifications()
            # Reset the notification generation time
            notification_generation_time = current_time + notification_generation_time_delta

# Start the heartbeat
print("Starting Heartbeat Service...\n")
heartbeat()
