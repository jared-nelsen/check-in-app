from flask import jsonify, make_response, request, json, g
import uuid
import dateutil.parser
import datetime as datetime
import json

from app import app
from app.api import getQuestion, storeAnswerOnBackEnd, getUserProfile, persistUserProfile, createNewUserProfile, generateUUID

@app.route('/retrieve-question', methods=['GET'])
def retrieveQuestion():
    # Get the session ID
    session_id = request.args.get('session_id')
    # Get the question index
    question_index = request.args.get('index')
    # Get the last answer
    last_question_answer = request.args.get('answer')
    # Get the question from the API
    question = getQuestion(session_id, question_index, last_question_answer)
    # Form the response body
    response_body = {
        "question": question
    }
    # Return the response
    return make_response(jsonify(response_body), 200)

@app.route('/store-answer', methods=['GET','POST'])
def storeAnswer():
    # Get the session ID
    session_id = request.args.get('session_id')
    # Get the question
    question = request.args.get('question')
    # Get the answer
    answer = request.args.get('answer')
    # Store the answer via the API
    storeAnswerOnBackEnd(session_id, question, answer)
    # Form the response body
    response_body = {
        "result": "success"
    }
    # Return the response
    return make_response(jsonify(response_body), 200)

@app.route('/retrieve-user-profile', methods=['GET', 'POST'])
def retrieveUserProfile():
    # The dummy User ID =1
    user_id = '1'
    # Retrieve JSON from the database
    user_profile = getUserProfile(user_id)
    # The Response is the user profile
    response_body = user_profile
    # Return the response
    return make_response(jsonify(response_body), 200)


@app.route('/save-user-profile', methods=['GET', 'POST'])
def saveUserProfile():
    # The dummy User ID = 1
    user_id = '1'
    # Get the email
    email = request.args.get('email')
    # Get the check in time (ISO 8601 String)
    check_in_time = dateutil.parser.parse(request.args.get('check_in_time'))
    # Persist new User Profile information
    persistUserProfile(user_id, email, check_in_time)
    # Form the response body
    response_body = {
        "result": "success"
    }
    return make_response(jsonify(response_body), 200)

@app.route('/create-default-user-profile', methods=['GET', 'POST'])
def createDefaultUserProfile():
    # The Default User Profile ID = 1
    user_id = '1'
    # The Default User Profile email is my email
    email = 'jnelsen788@gmail.com'
    # The Default User Profile Check In Time is now
    check_in_time = datetime.datetime.now().isoformat()
    # Persist new User Profile information
    createNewUserProfile(user_id, email, check_in_time)
    # Form the response body
    response_body = {
        "result": "success"
    }
    return make_response(jsonify(response_body), 200)

@app.route('/create-random-user-profile', methods=['GET', 'POST'])
def createRandomUserProfile():
    # Generate a random id
    user_id = generateUUID()
    # Set my email
    email = 'jnelsen788@gmail.com'
    # Get the check in time from the console
    check_in_time = request.args.get('check_in_time')
    # Persist it
    createNewUserProfile(user_id, email, check_in_time)
    # Form the response body
    response_body = {
        "result": "success"
    }
    return make_response(jsonify(response_body), 200)
