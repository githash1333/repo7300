import requests
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import uuid
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
