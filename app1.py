from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import logging
#uvicorn app1:app --reload

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Notification(BaseModel):
    title: str
    body: str
    target_url: str

@app.post("/send-notification")
async def send_notification(notification: Notification):
    try:
        response = requests.post(notification.target_url, json={"title": notification.title, "body": notification.body})
        response.raise_for_status()
        return {"status": "success", "detail": response.json()}
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        raise HTTPException(status_code=response.status_code, detail=str(http_err))
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        raise HTTPException(status_code=502, detail="Connection error occurred.")
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        raise HTTPException(status_code=504, detail="Timeout error occurred.")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
        raise HTTPException(status_code=500, detail="Internal Server Error.")

