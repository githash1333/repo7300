import firebase_admin
from firebase_admin import credentials, messaging , firestore
from pymongo import MongoClient

# # Initialize the Firebase app
# cred = credentials.Certificate("servicejson.json")
# firebase_admin.initialize_app(cred)

# # Get a JWT token
# token = cred.get_access_token()
# print("********************************************************")
# print(token)
# print("********************************************************")

# Initialize the Firestore client
# db = firestore.client()

# Function to send push notifications
def send_push_notification(registration_token, title, body):

    

    message = messaging.Message(
    notification=messaging.Notification(
    title=title,
    body=body,
    ),
    token=registration_token,
)

# Send a message to the device corresponding to the provided
# registration token.
    response = messaging.send(message)
    return print('Successfully sent message:', response)

import requests
import json
from bson import ObjectId
def serialize_document(doc):
    if '_id' in doc and isinstance(doc['_id'],ObjectId):
        doc['_id'] = str(doc['_id'])
    return doc


def send(document):
    # Initialize Firebase Admin SDK

    document = serialize_document(document)
    url = "https://ap-south-1.aws.data.mongodb-api.com/app/data-bkrdaiv/endpoint/data/v1/action/findOne"

    payload = json.dumps({
        "collection": "ClientCollection",
        "database": "ClientDB",
        "dataSource": "Cluster0",
        "projection": document
    })
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'MWLR5zxRiO8c4MkqSElua7J95do7i92Kg7sCdPduS53QnBGyonPBheaxnOPSFbpX',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    

    response_dict = response.text


    print(response_dict)
    import ast
    try:
        dict_obj = ast.literal_eval(response_dict)

        print("***********")

        print(dict_obj)

        print(type(dict_obj))
    except:
        pass

    # Fetch data from MongoDB
    # devices = collection.find()
    # print(devices)

# Iterate through the devices and send notifications
    
    registration_token = dict_obj['document']['fcm_token']
    title = 'VM-Title'
    body = 'Your Notification Body'
    send_push_notification(registration_token, title, body)

    return


