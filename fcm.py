




from email import message
import pyfcm

def push_n(device_token,n_payload):
    api_key = "AIzaSyCtqRY1ienG1r8cf9gQB19vCHbhnO9vnYA"

    sender_id = "730958777059"

    push_service = pyfcm.FCMNotification(api_key ,sender_id)

    message = push_service.async_notify_multiple_devices(registration_id = device_token,message_title = n_payload['title'],
    message_body = n_payload['body'])

    return ('sent' , message)
