import dateutil.parser
import datetime

from app import db

def sendNotification(notification):
    print("\nNotification Sent!")
    print("----------------------------------------------------------")
    print(notification)
    print("----------------------------------------------------------")

def generateAndSendNotifications():
    # Get the collection reference
    collection = db.collection('notifications')
    # Filter by notifications that have not been sent
    ref = collection.where('sent', '==', False)
    # Get the stream of data
    notifications = ref.stream()
    # Send each notification
    for notification in notifications:
        # Convert it to a dict
        notification = notification.to_dict()
        # Check if check in time has passed
        check_in_time = dateutil.parser.parse(notification['check_in_time'])
        if check_in_time < datetime.datetime.now():
            # Send the notification
            sendNotification(notification)
            # Get the notification id
            notification_id = notification['id']
            # Grab the document for this notification
            ref = collection.document(notification_id)
            # Update it to be sent
            ref.update({'sent': True})
