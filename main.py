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
import subprocess
import socket
warnings.filterwarnings('ignore')




base = st.title("SignUp/Login")

ph_number = st.text_input("Enter a Phone Number",placeholder="+91",max_chars=10)
import requests

# if ph_number!='' or len(ph_number)!=0:
if st.button("Get OTP / Login") and len(ph_number)!=0:
    recipient_number =   "+91"+str(ph_number)


    # try:
    #     cred = credentials.Certificate(r"servicejson.json")

    #     firebase_admin.initialize_app(cred)

    #     fcm_client = messaging.Client()

    #     print(fcm_client)
    # except:
    #     pass


    # # Run the command to get the current working directory
    # result = subprocess.run(['cd'], capture_output=True, text=True, shell=True)
    # cwd = result.stdout

    # st.text(str(cwd))
    # # cwd = cwd.replace('\n','')
    # # Print the output
    # filepath = r"fcm.py"
    # # import subprocess

    # # Define the command to run the Python script
    # command = ['python', filepath]

    # # Run the command
    # result = subprocess.Popen(command, text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    # # Print the output

    # print(result.stdout)

    # st.text("Flask app is running.....")

    








    # URL of the Flask app endpoint
    import time
    time.sleep(60)
    
    
    url = 'http://127.0.0.1:8421/get-data'

    # Make a GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        st.header("Response JSON:")
        st.text(data)
    else:
        st.header("Failed to fetch data")
        print(f"Status code: {response.status_code}")



    try:


    
        url = "https://ap-south-1.aws.data.mongodb-api.com/app/data-bkrdaiv/endpoint/data/v1/action/insertOne"

        payload = json.dumps({
            "collection": "ClientCollection",
            "database": "ClientDB",
            "dataSource": "Cluster0",
            "document": data
        })
        headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': 'MWLR5zxRiO8c4MkqSElua7J95do7i92Kg7sCdPduS53QnBGyonPBheaxnOPSFbpX',
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        st.text(response.text)
    except:
        pass
    
        # device_token = messaging._get_messaging_service



    # try:
    #     import os
    #     from google.oauth2 import service_account
    #     from googleapiclient.discovery import build

    #     creds = service_account.Credentials.from_service_account_file(r"servicejson.json")
    #     fcm_service = build('fcm','v1',credentials=creds)
    #     token = mongo.device_res_id()
    #     try:
    #         normal_string = token.decode('uft-8')
    #     except:
    #         pass
    #     print(normal_string)
    #     message = {
    #         'data':{
    #             'score':'850',
    #             'time':'2:45'
    #         },
    #         'notification':{
    #             'title':'FCM',
    #             'body':'Notification'
    #         },
    #         'token':normal_string
    #     }
    #     response = fcm_service.projects().message().send(name = 'projects/fir-ca40d/messages:send',body = message).execute()
    #     print(response)    #     # Your service account key file
    # #     service_account_file = 'servicejson.json'

    #     # cred = credentials.Certificate("servicejson.json")
    #     # firebase_admin.initialize_app(cred,{"projectid":"fir-ca40d"})
    #     # device_token = messaging._get_messaging_service
    # except: 
    #     pass

    #     # Scopes required by the API
    #     scopes = ['https://www.googleapis.com/auth/cloud-platform']

    #     # Load the service account credentials
        # credentials_ = google.auth.load_credentials_from_file(service_account_file, scopes=scopes)[0]
    #     print(credentials_)
    #     # Define the JWT payload
    #     payload = {
    #     'iss': credentials_.service_account_email,
    #     'sub': credentials_.service_account_email,
    #     'aud':  'https://your-api-endpoint.com',
    #     'iat': int(time.time()),
    #     'exp': int(time.time()) + 3600 # Token expiry time (1 hour)
    #     }

    #     # Sign the JWT
    #     signed_jwt = jwt.encode(credentials_.signer, payload)


    #     print(str(signed_jwt))

    #     print(type(signed_jwt))

    #     # Decode the byte string to a regular string
    #     regular_string = signed_jwt.decode('utf-8')

    #     regular_string = r"{}".format(regular_string)
    #     print(regular_string)

    #     # Use the signed JWT for authentication
    #     headers = {'Authorization': f'Bearer {regular_string}'}

    #     try:
    #         validated_token = validate_token(regular_string)
    #         # Use the validated token
    #     except ValueError as e:
    #         print(f"Error: {e}")

    # except:
    #     pass

    

    # # Initialize the Firebase Admin SDK
    # cred = credentials.Certificate(r'servicejson.json')
    # firebase_admin.initialize_app(cred)

    # custom_token = mongo.device_res_id()

    # print(custom_token)

    # custom_token = custom_token.decode('uft-8')

    # custom_token = r"{}".format(custom_token)


    

    

    # Example usage
    # device_token = signed_jwt
    # response = send_notification1(device_token, 'VM-Test', 'Test Body')
    # print('Successfully sent message:', response)






    

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
    import time
    time.sleep(10)

    st.switch_page(r"pages/GetPhoneResponse.py")


    





    




