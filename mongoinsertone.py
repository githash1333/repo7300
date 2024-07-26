
import requests
import json
import uuid


url = "https://ap-south-1.aws.data.mongodb-api.com/app/data-bkrdaiv/endpoint/data/v1/action/insertOne"

payload = json.dumps({
    "collection": "ClientCollection",
    "database": "ClientDB",
    "dataSource": "Cluster0",
    "projection": {
        "id": str(uuid.uuid1())
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'MWLR5zxRiO8c4MkqSElua7J95do7i92Kg7sCdPduS53QnBGyonPBheaxnOPSFbpX',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)