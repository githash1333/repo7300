from pymongo import MongoClient
from stitch import Stitch
#public_key = "lesqbftu"
# Private_Key = "3fd41b4e-18d2-413f-9963-6ee154157831" 
# Initialize the MongoDB Stitch client
client = Stitch(appid="application-1-bfprsga",apikey="3fd41b4e-18d2-413f-9963-6ee154157831")

# Get a reference to the Push Notifications service
push_service = client.get_service("push")

# Define the notification payload
notification = {
    "title": "Test Notification",
    "message": "This is a test notification"
}

# Define the target audience for the notification
audience = {
    "users": ["user1", "user2"]
}

# Send the push notification
push_service.send(notification, audience)