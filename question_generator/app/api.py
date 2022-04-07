import uuid

from app import db
from app.questions import *

def generateUUID():
    return uuid.uuid4().hex

# THIS WILL EVENTUALLY TAKE IN THE ANSWER TO THE LAST QUESTION
# AND BE ABLE TO GENERATE A FOLLOW UP QUESTION
def getQuestion(session_id, conversation_index, last_question_answer):

    # 1. Get and order the Session Plan Steps for the Session ID
    # -------------------------------------------------------------------------------------------------
    # Get the Session Plan Steps collection
    collection = db.collection('session_plan_steps')
    # Filter to the session id
    ref = collection.where('session_id', '==', session_id)
    # Get the Session Plan Steps
    session_plan_steps_results = ref.get()
    # Transform them into a list of dictionaries
    session_plan_steps = []
    for session_plan_steps_result in session_plan_steps_results:
        session_plan_steps.append(session_plan_steps_result.to_dict())
    # Sort the list of Session Plan Steps by Conversation Step Index
        # The Session plan steps are now ordered by Conversation Step Index and we can access them by
        # the given conversation_index variable with guaranteed order
    session_plan_steps = sorted(session_plan_steps, key = lambda i: (i['conversation_step_index']))

    # 2. Select the Question Type index from the given Session Plan Step indicated by
    #    the conversation index
    # -------------------------------------------------------------------------------------------------
    # Select the Session Plan Step in question
    session_plan_step = session_plan_steps[int(conversation_index)]
    # Retrieve the type indicator for the conversation step from the session plan step
    question_type = session_plan_step['conversation_step_question_type']
    
    # 3. Generate a question
        # Generate a question using a switch like apparatus
        # where each case calls a function to generate that
        # question type. For now I can just select a
        # predefined question for each type. A next step might
        # be to randomly select from a list of questions of that
        # type. A stretch goal would be to add logic there to
        # retrieve past questions and avoid asking the same
        # one again.
    # -------------------------------------------------------------------------------------------------
    question = "Default Question"
    if question_type == 0:
        question = getGenericQuestion()
    elif question_type == 1:
        question = getElaborativeQuestion()
    else:
        question = "Unspecified question indicator type"
    # Return the question
    return question
