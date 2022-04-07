import uuid
import requests
import json

from app import db

# URIs
question_generator_generate_question_url = 'http://localhost:5004/generate-question'

def generateUUID():
    return uuid.uuid4().hex

def getQuestion(session_id, question_index, last_question_answer):
    # Form the parameters to the question generator
    question_params = {
                       "session_id": session_id, 
                       "conversation_index": question_index, 
                       "last_question_answer": last_question_answer
                      }
    # Request the question from the question generator
    question_response = requests.get(question_generator_generate_question_url, params=question_params)
    # Unpack the question
    question = json.loads(question_response.text)['question']
    # Return in
    return question

def storeAnswerOnBackEnd(sessionID, question, answer):
    # Get the collection
    collection = db.collection('answers')
    # Create a new unique id
    uuid = generateUUID()
    # Define the document
    ref = collection.document(uuid)
    # Make the answer
    answer = {"uuid": uuid, "session_id": sessionID, "question": question, "answer": answer}
    # Persist the answer
    ref.set(answer)

def getUserProfile(user_id):
    # Get the user profile collection
    collection = db.collection('user_profile')
    # Filter to the user profile id
    ref = collection.where('user_id', '==', user_id)
    # Get the user profile
    user_profile = ref.get()[0].to_dict()
    # Return it
    return user_profile

def persistUserProfile(user_id, email, check_in_time):
    # Get the user profile collection
    collection = db.collection('user_profile')
    # Filter the the user profile id
    ref = collection.document(user_id)
    # Update the fields
    ref.update({'id': user_id, 'email': email, 'check_in_time': check_in_time})

def createNewUserProfile(user_id, email, check_in_time):
    # Get the user profile collection
    collection = db.collection('user_profile')
    # Define the document
    ref = collection.document(user_id)
    # Persist the document
    ref.set({'user_id': user_id, 'email': email, 'check_in_time': check_in_time})
