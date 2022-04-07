import uuid
from datetime import datetime

from app import db

def generateUUID():
    return uuid.uuid4().hex

def retrieveAllUserProfiles():
    # Get the reference to the user profile collection
    ref = db.collection('user_profile')
    # Get all user profiles
    user_profile_documents = ref.get()
    # Convert them to a list of dicts
    user_profiles = []
    for doc in user_profile_documents:
        user_profiles.append(doc.to_dict())
    # Return the user profiles
    return user_profiles

def generateSessionData(session_id, user_profile):
    # Mark the generation of the session
    session_generated_date = datetime.now().isoformat()
    # Retrieve the check in time from the user profile
    check_in_time = user_profile['check_in_time']
    # Define the session
    session = {"id": session_id, "check_in_time": check_in_time, "generated_date": session_generated_date}
    # Get the collection reference
    ref = db.collection('sessions')
    # Define the document
    ref = ref.document(session_id)
    # Persist the session
    ref.set(session)

def generateSessionPlan(session_id, session_plan_id, user_profile):
    # Get the user id
    user_id = user_profile['user_id']
    # Define the Session Plan
    session_plan = {"session_id": session_id, "id": session_plan_id, "user_id": user_id}
    # Get the collection reference
    ref = db.collection('session_plans')
    # Define the document
    ref = ref.document(session_plan_id)
    # Persist the Session Plan
    ref.set(session_plan)

def generateSessionPlanSteps(session_id, session_plan_id):
    # Generate a list of session step types
        # HERE IS WHERE I CAN PULL FROM A PREFERENCES TABLE
    step_type_indicators = [0, 1, 0]
    # For every step
    for i in range(len(step_type_indicators)):
        # Generate a UUID for the Session Plan Step
        session_plan_step_id = generateUUID()
        # Set the conversation step index
        conversation_step_index = i
        # Define the Session Plan Step
        session_plan_step = {
            "id": session_plan_step_id, 
            "session_id": session_id, 
            "session_plan_id": session_plan_id,
            "conversation_step_question_type": step_type_indicators[i],
            "conversation_step_index": conversation_step_index
            }
        # Get the collection reference
        ref = db.collection('session_plan_steps')
        # Define the document
        ref = ref.document(session_plan_step_id)
        # Persist the Session Plan Step
        ref.set(session_plan_step)

def scheduleNotification(session_id, user_profile):
    # Define a notification id
    notification_id = generateUUID()
    # Define the notification
    notification = {
                    "id": notification_id,
                    "sent": False,
                    "session_id": session_id, 
                    "check_in_time": user_profile['check_in_time'], 
                    "user_id": user_profile['user_id']
                    }
    # Get the collection reference
    ref = db.collection('notifications')
    # Define the document
    ref = ref.document(notification_id)
    # Persist the notification
    ref.set(notification)

def generateSession(session_id, user_profile):
    # Generate the session data
    generateSessionData(session_id, user_profile)
    # Generate the Session Plan ID
    session_plan_id = generateUUID()
    # Generate the Session Plan
    generateSessionPlan(session_id, session_plan_id, user_profile)
    # Generate the Session Plan Steps
    generateSessionPlanSteps(session_id, session_plan_id)
    # Schedule notification
    scheduleNotification(session_id, user_profile)
