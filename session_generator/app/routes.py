import datetime as datetime
from flask import jsonify, make_response, request, json

from app import app
from app.utilities import liesWithinNextHour
from app.api import retrieveAllUserProfiles, generateSession, generateUUID

@app.route('/generate-sessions', methods=['GET','POST'])
def generateSessions():
    # Retrieve all User Profiles
    user_profiles = retrieveAllUserProfiles()
    # For each User Profile
    for user_profile in user_profiles:
        # Generate a Session ID
        session_id = generateUUID()
        # Select the check in time
        check_in_time = user_profile["check_in_time"]
        # Detect if it lies within the next hour
        lies_within_next_hour = liesWithinNextHour(check_in_time)
        # If it does lie within the next hour
        if lies_within_next_hour:
            generateSession(session_id, user_profile)
    # Form the response body
    response_body = {
        "result": "success",
        "session_generation_finish_time": datetime.datetime.now(),
        "session_generation_count": len(user_profiles)
    }
    # Return the result
    return make_response(jsonify(response_body), 200)

@app.route('/generate-session', methods=['GET','POST'])
def generateSingleSession():
    # See if there is a session id passed (from the local dev environment)
    session_id = request.args.get('session_id')
    if session_id is None:
        # Generate a Session ID
        session_id = generateUUID()
    # Retrieve the user profile
    user_profile = json.loads(request.args.get('user_profile'))
    # Generate the Session through the API
    generateSession(session_id, user_profile)
    # Form the response body
    response_body = {
        "result": "success",
        "session_id": session_id
    }
    # Return the result
    return make_response(jsonify(response_body), 200)
