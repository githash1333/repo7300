
from xml.dom.minidom import Document

from pymongo.mongo_client import MongoClient



# from pymongo.mongo_client import MongoClient

# uri = "mongodb+srv://dbuser:dbpassword@cluster0.kycczp4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

# uri = "mongodb+srv://dbuser:dbpassword@cluster0.kycczp4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


# # List all databases on the server
# databases = client.list_database_names()

# # Print the list of databases
# print("Databases on the server:")

# for db_name in databases:
#     print(db_name)



def createdbInsertOne(documents):

    uri = "mongodb+srv://dbuser:dbpassword@cluster0.kycczp4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
    client = MongoClient(uri)

    # try:

    db = client['ClientDB']

    collection = db["ClientCollection"]

    collection.insert_one(documents)
    # except:
        # print("Failed to insert")

    return "Success"


# from pymongo import MongoClient
def fetchdocuments():
# Create a MongoClient instance
    uri = "mongodb+srv://dbuser:dbpassword@cluster0.kycczp4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
    client = MongoClient(uri)

    # Select the database
    db = client['ClientDB']

    # Select the collection
    collection = db['ClientCollection']


    # print(collection)

    documents = collection.find()

    for document in documents:
        print(document)
        print(len(document))

    return collection

    # Fetch all documents in the collection
    # documents = collection.find()

    # # Iterate over the documents
    # for document in documents:
    #     print(document)

    # documents = collection.find({'name': 'John'})
    

# fetchdocuments()

import secrets
import string

def generate_random_string(length: int) -> str:
    """
    Generate a random string of a given length.

    Args:
        length (int): The length of the random string.

    Returns:
        str: A random string of the specified length.
    """
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


import firebase_admin
from firebase_admin import credentials,messaging , auth
from datetime import datetime
def device_res_id():
    project_id = "fir-ca40d"


    print(credentials.AccessTokenInfo.mro())
    current = str(datetime.now())
    print(firebase_admin.datetime.datetime.fromisoformat(current))

    cred = credentials.Certificate(r"servicejson.json")

    firebase_admin.initialize_app(cred , {"Projectid":project_id})

    custom_token = auth.create_custom_token('user_id')


    # print(custom_token)
    return custom_token


# DEVICE_TOKEN = messaging.get_registration_token()
# fcm = messaging.firebase_admin.App()
# print(fcm)
# print(DEVICE_TOKEN)
# messaging.



