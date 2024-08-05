
from email import message
import os
import json 
from firebase_admin import credentials  , messaging , auth
import firebase_admin


import mongo

token = mongo.device_res_id()
import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.exceptions import InvalidSignature

# Your RSA private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Your RSA public key
public_key = private_key.public_key()

# Payload data
payload = {
        'title':'FCM',
        'body':'2:45'
    }

# Serialize the public key
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Generate a JWT
encoded_jwt = jwt.encode(payload, private_key, algorithm='RS256')
print(f'Encoded JWT: {encoded_jwt}')

# Deserialize the public key
public_key = serialization.load_pem_public_key(
    pem
)

# Validate the JWT
try:
    decoded_payload = jwt.decode(encoded_jwt, public_key, algorithms=['RS256'],verify=True)
    print('JWT is valid')
    print(f'Decoded payload: {decoded_payload}')
except jwt.ExpiredSignatureError:
    print('JWT signature has expired')
except jwt.InvalidTokenError:
    print('JWT is invalid')


# Initialize Firebase Admin SDK with service account
# cred = credentials.Certificate(r'servicejson.json')
# firebase_admin.initialize_app(cred)
# encoded_jwt = auth.verify_id_token(encoded_jwt)
message1 = messaging.Message(
    # data = {
    #     'scope':'850',
    #     'time':'2:45'
    # },
    notification=messaging.Notification(
        title="FCM",
        body='This is a instance'
    ),
    token = encoded_jwt
)

response = messaging.send(message1,dry_run=False)

print(response)