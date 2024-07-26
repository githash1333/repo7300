import requests
import json


def findDataMongo(document):
    url = "https://ap-south-1.aws.data.mongodb-api.com/app/data-bkrdaiv/endpoint/data/v1/action/findOne"

    payload = json.dumps({
        "collection": "ClientCollection",
        "database": "ClientDB",
        "dataSource": "Cluster0",
        "projection": document
    })
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'MWLR5zxRiO8c4MkqSElua7J95do7i92Kg7sCdPduS53QnBGyonPBheaxnOPSFbpX',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    response_dict = response.text

    return response_dict


# findDataMongo("+919326332776")