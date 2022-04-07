# Console App

import requests
import uuid
from datetime import datetime, timedelta

# This app contains functionality for local development

# UI Front End Enpoints
front_end_landing_page_url_local = 'http://localhost:5555/#/land'
# UI Back End Endpoints
ui_back_end_server = 'http://localhost:5001'
ui_back_end_server_create_default_user_profile = ui_back_end_server + '/create-default-user-profile'
ui_back_end_server_retrieve_default_user_profile = ui_back_end_server + '/retrieve-user-profile'
ui_back_end_server_generate_random_user_profile = ui_back_end_server + '/create-random-user-profile'
# Session Generator Endpoints
session_generator_server = 'http://localhost:5003'
session_generator_generate_sessions = session_generator_server + '/generate-session'

# ----------------------------------------------------------------------------------------------------
# Sessions
# ----------------------------------------------------------------------------------------------------

def generateUUID():
    return uuid.uuid4().hex

# Generates a session through the session generator
def newSession():
    # Retrieve the default user profile
    user_profile = requests.get(ui_back_end_server_retrieve_default_user_profile)
    user_profile = user_profile.text
    # Generate a Session ID to pass for testing purposes
    session_id = generateUUID()
    # Load it into params
    params = {"user_profile": user_profile, "session_id": session_id}
    # params = {'session_id': session_id}
    requests.get(session_generator_generate_sessions, params=params)
    # Create the session url
    session_url = front_end_landing_page_url_local + '?id=' + session_id
    # Print it for use
    print(session_url)

# ----------------------------------------------------------------------------------------------------
# User Profiles
# ----------------------------------------------------------------------------------------------------
def createDefaultUserProfile():
    requests.get(ui_back_end_server_create_default_user_profile)

def generateRandomTimeSeriesUserProfiles():
    count = int(input("How many user profiles?\n"))
    check_in_time = datetime.now() + timedelta(seconds=30)
    for x in range(count):
        x = x
        check_in_time = check_in_time + timedelta(seconds=15)
        params = {"check_in_time": check_in_time.isoformat()}
        requests.get(ui_back_end_server_generate_random_user_profile, params=params)

# ----------------------------------------------------------------------------------------------------

prompt = "What would you like to do?\n"
prompt += "1. Create Default User Profile\n"
prompt += "2. Generate random user profiles\n"
prompt += "3. Create Session through Session Generator\n"
selection = input(prompt)

if selection == "1":
    createDefaultUserProfile()
elif selection == "2":
    generateRandomTimeSeriesUserProfiles()
elif selection == "3":
    newSession()