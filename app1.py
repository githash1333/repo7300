from flask import Flask, request
from pyfcm import FCMNotification

app = Flask(__name__)

# Initialize the FCM notification service
push_service = FCMNotification(service_account_file=r"servicejson.json",project_id="fir-ca40d")

# Define a route to push notifications
@app.route("/push_notification", methods=["POST"])
def push_notification():
    # Get the device token from the request
    device_token = request.json["device_token"]

    # Define the notification message
    message_title = "VM-Test"
    message_body = "This is a test notification"

    # Push the notification to the device
    result = push_service.async_notify_multiple_devices(
        registration_id=device_token,
        message_title=message_title,
        message_body=message_body
    )

    # Return the result of the push notification
    return result

if __name__ == "__main__":
    app.run(debug=True)