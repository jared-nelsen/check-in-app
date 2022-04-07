from flask import jsonify, make_response

from app import app
from app.api import generateAndSendNotifications

@app.route('/generate-notifications', methods=['GET','POST'])
def generateNotifications():
    # Generate and send notifications
    generateAndSendNotifications()
    # Form the response body
    response_body = {
        "result": "success"
    }
    # Return the result
    return make_response(jsonify(response_body), 200)
