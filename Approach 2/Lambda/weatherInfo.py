import json
import logging
from botocore.vendored import requests

def lambda_handler(event, context):
    # TODO implement
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # logger.info("Testing Logger", event)
    
    getData = requests.get("https://j9l4zglte4.execute-api.us-east-1.amazonaws.com/api/ctl/weather")
    logger.info("Testing getData", getData.json())
    
    print(getData)
    data = getData.json()
    city = data["today"]["city"]
    logger.info("Testing city")
    logger.info(city)
    state = data["today"]["state"]
    desc = data["today"]["description"]
    
    desc1 = data["daily"][0]["description"]
    lowTemp1 = data["daily"][0]["lowTemperature"]
    highTemp1 = data["daily"][0]["highTemperature"]
    
    desc2 = data["daily"][1]["description"]
    lowTemp2 = data["daily"][1]["lowTemperature"]
    highTemp2 = data["daily"][1]["highTemperature"]
    
    desc3 = data["daily"][2]["description"]
    lowTemp3 = data["daily"][2]["lowTemperature"]
    highTemp3 = data["daily"][2]["highTemperature"]
    
    print(city)
    print(state)
    print(desc)
    print("desc1: ", desc1, "lowTemp1:", lowTemp1, "highTemp1:", highTemp1)
    print("desc2: ", desc2, "lowTemp2:", lowTemp2, "highTemp2:", highTemp2)
    print("desc3: ", desc3, "lowTemp3:", lowTemp3, "highTemp3:", highTemp3)
    # print(response['today']['state'])
    
    response = {}
    response['city'] = city
    response['state'] = state
    response['description'] = desc
    response['next3DaysInfo'] = []
    response['next3DaysInfo'].append({'description': desc1, 'Low Temperature': lowTemp1, 'High Temperature': highTemp1})
    response['next3DaysInfo'].append( {'description': desc2, 'Low Temperature': lowTemp2, 'High Temperature': highTemp2})
    response['next3DaysInfo'].append({'description': desc3, 'Low Temperature': lowTemp3, 'High Temperature': highTemp3})
    
    # [{'description': desc1, 'Low Temperature': lowTemp1, 'High Temperature': highTemp1}, 
    #                              {'description': desc2, 'Low Temperature': lowTemp2, 'High Temperature': highTemp2}, 
    #                              {'description': desc3, 'Low Temperature': lowTemp3, 'High Temperature': highTemp3}]
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

