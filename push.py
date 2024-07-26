import os
# from termios import tcdrain
from pyfcm import FCMNotification
import warnings
warnings.filterwarnings('ignore')
# api_key = "AIzaSyCtqRY1ienG1r8cf9gQB19vCHbhnO9vnYA"
push_service = FCMNotification(r"servicejson.json",project_id="fir-ca40d")

# print(push_service)
async def get_user_device_registration_id(recipient_number , user_collection):
    user = await user_collection.find_one({"recipientNumber":recipient_number})
    if user:
        return user.get("device_registration_id")

    return None

from motor.motor_asyncio import AsyncIOMotorClient


async def push_post(recipient_number):
    client = AsyncIOMotorClient(r"mongodb+srv://dbuser:dbpassword@cluster0.kycczp4.mongodb.net/")

    db = client.get_database("ClientDB")

    user_collection = db.get_collection("ClientCollection")



    # td = ''
    registration_id = get_user_device_registration_id(recipient_number , user_collection)

    print("registration_id - ",registration_id)

    if registration_id != None:
        message_title = 'VM-TEST'
        message_body = '**This is a test Body**'

        result = push_service.async_notify_multiple_devices(registration_id , message_title , message_body )
        print(result)
    return  result

recipient_number = "+919321550748"
push_post(recipient_number)