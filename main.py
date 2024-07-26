import pandas as pd
import os
import streamlit as st
import json 
import random
import uuid
import mongo
import mongofindone
import push
import ast
import warnings
import fcm
import subprocess
# import player
import requests
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
warnings.filterwarnings('ignore')
base = st.title("SignUp/Login")

ph_number = st.text_input("Enter a Phone Number",placeholder="+91",max_chars=10)
import requests









def send_notification(ip_address, port, endpoint, title, body):
    url = f"http://{ip_address}:{port}/{endpoint}"
    payload = {
        "title": title,
        "body": body
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        logger.info(f"Successfully sent notification to {ip_address}:{port}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
    return

import socket

def get_local_ip_address():
    try:
        # Connect to an external server to get the local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Using Google DNS server address
        local_ip_address = s.getsockname()[0]
        s.close()
        return local_ip_address
    except Exception as e:
        print(f"Unable to get local IP address: {e}")
        return None

# print("Local IP Address:", get_local_ip_address())
import firebase_admin
from firebase_admin import credentials, messaging
def send_notification1(token, title, body):
    if not isinstance(token, str) or not token:
        raise ValueError("Invalid token: must be a non-empty string.")
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token,
    )
    response = messaging.send(message)
    return response



uid = str(uuid.uuid1())
import google.auth
from google.auth import jwt
import time
# if ph_number!='' or len(ph_number)!=0:
if st.button("Get OTP / Login") and len(ph_number)!=0:
    recipient_number =   "+91"+str(ph_number)

    try:

        # Your service account key file
        service_account_file = 'servicejson.json'

        cred = credentials.Certificate("servicejson.json")
        firebase_admin.initialize_app(cred)

        # Scopes required by the API
        scopes = ['https://www.googleapis.com/auth/cloud-platform']

        # Load the service account credentials
        credentials_ = google.auth.load_credentials_from_file(service_account_file, scopes=scopes)[0]
        print(credentials_)
        # Define the JWT payload
        payload = {
        'iss': credentials_.service_account_email,
        'sub': credentials_.service_account_email,
        'aud':  'https://your-api-endpoint.com',
        'iat': int(time.time()),
        'exp': int(time.time()) + 3600 # Token expiry time (1 hour)
        }

        # Sign the JWT
        signed_jwt = jwt.encode(credentials_.signer, payload)


        print(str(signed_jwt))

        print(type(signed_jwt))

        # Decode the byte string to a regular string
        regular_string = signed_jwt.decode('utf-8')

        regular_string = r"{}".format(regular_string)

        # Use the signed JWT for authentication
        headers = {'Authorization': f'Bearer {regular_string}'}

    except:
        pass

    

    # # Initialize the Firebase Admin SDK
    # cred = credentials.Certificate(r'servicejson.json')
    # firebase_admin.initialize_app(cred)

    # custom_token = mongo.device_res_id()

    # print(custom_token)

    # custom_token = custom_token.decode('uft-8')

    # custom_token = r"{}".format(custom_token)


    

    

    # Example usage
    device_token = signed_jwt
    response = send_notification1(device_token, 'VM-Test', 'Test Body')
    print('Successfully sent message:', response)






    

    # from firebase_admin import credentials
    # import firebase_admin

    

        


        

        

    #     document = {"UID":uid , "recipientNumber":recipient_number,"fcm_token":str(regular_string)}

    #     print(document)

    #     response_dict = mongo.createdbInsertOne(document)

    #     print(response_dict)

    #     print(type(response_dict))

    #     try:
    #         dict_obj = ast.literal_eval(response_dict)

    #         print("***********")

    #         print(dict_obj)

    #         print(type(dict_obj))
    #     except:
    #         pass
    # except:
    #     pass


    # #findDataMongo(document)



    # # if len(dict_obj)!=0:
    # #     myvariable = dict_obj['document']['recipientNumber']

    # #     device_token = dict_obj['document']['fcm_token']
    # #     # myvariable = new_dict['recipientNumber']

    # #     print(device_token)

    # import firebase_push
    # try:
    #     firebase_push.send(document)
    #     print("success")
    # except:
    #     print("Failed")

    # try:
    #     import requests
    #     import logging

    #     # Configure logging
    #     logging.basicConfig(level=logging.INFO)
    #     logger = logging.getLogger(__name__)

    #     ip = get_local_ip_address()

        

    #     # Example usage
    #     ip_addresses = [
    #         {"ip": f"{ip}", "port": 8085, "endpoint": "notify"},
    #     ]

    #     for device in ip_addresses:
    #         send_notification(device["ip"], device["port"], device["endpoint"], "VM-TEST", "This is a test notification.")
    # except:
    #     pass
        # try:
        #     firebase_push.send_push_notification()

        # result = push.push_post(document["recipientNumber"])

        # print(result)

        # n_payload = {'title':'VM-TEST','body':'**This is a test**'}

        # fcm.push_n(device_token ,n_payload)



    # try:
    #     mongo.createdbInsertOne(document)
    # except:
    #     print("Failed to Insert")
    #     pass


    # collection = mongo.fetchdocuments()
    # try:
    #     documents = collection.find({'recipientNumber': recipient_number})
    # except:
    #     pass

    # print(documents)

    # if len(documents)!=0:
    #     push.push_post(document["recipientNumber"])
    # else:
    #     try:
    #         mongo.createdbInsertOne(document)
    #     except:
    #         print("Failed to Insert")
    #         pass



    # Fetch all documents in the collection
    # documents = collection.find()

    # # # Iterate over the documents
    # for document in documents:
    #     print(document)


    # 

    st.switch_page(r"pages/GetPhoneResponse.py")


    





    




