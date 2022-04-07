from flask import jsonify, make_response, request, json, g
import dateutil.parser
import json
import requests

from app import app
from app.api import getQuestion

@app.route('/generate-question', methods=['GET', 'POST'])
def generateQuestion():
    # Get the Session ID
    session_id = request.args.get('session_id')
    # Get the index of the question in the conversation
    conversation_index = request.args.get('conversation_index')
    # Get the answer to the last question
    # CORNER CASE: THE FIRST QUESTION, index 0, does not have an
    # answer with it
    last_question_answer = request.args.get('last_question_answer')
    # HERE IS WHERE I CAN USE THE ANSWER TO THE LAST QUESTION
    # TO ASK A FOLLOW UP QUESTION
    # Get the question based on the session step indicator in
    # the database for the index of the conversation we are on
    question = getQuestion(session_id, conversation_index, last_question_answer)
    # Form the response body
    response_body = {
        "result": "success",
        "question": question
    }
    # Return the response
    return make_response(jsonify(response_body), 200)
    
