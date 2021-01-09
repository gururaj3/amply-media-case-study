from django.shortcuts import render
import requests
import requests_cache
import logging
import time
import json

# Create your views here.
from django.http import HttpResponse

requests_cache.install_cache('weather-info-cache', backend='sqlite', expire_after=180)

def index(request):
    return render(request, "weatherInfo/index.html")

def getInfo(request):

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # logger.info("Testing Logger", event)
    
    # URL = "http://maps.googleapis.com/maps/api/geocode/json"
    # location = "delhi technological university"
  
    # # defining a params dict for the parameters to be sent to the API 
    # PARAMS = {'address':location} 
  
    # # sending get request and saving the response as response object 
    # r = requests.get(url = URL, params = PARAMS) 
    # print(r.json())

    
    
    getData = requests.get("https://j9l4zglte4.execute-api.us-east-1.amazonaws.com/api/ctl/weather")
    logger.info("Testing getData", getData.json())
    
    print(getData)
    data = getData.json()
    # print "Time: {0} / Used Cache: {1}".format(now, response.from_cache)
    now = time.ctime(int(time.time()))
    print("time: ", now)
    print("cache: ", getData.from_cache)
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
    
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps(response)
    # }
    weatherData = json.dumps(response)
    print(weatherData)
    # console.log(weatherData)

    context = {
        "weatherData": weatherData,
        "city": city,
        "state": state,
        "desc": desc,
        "lowTemp1": lowTemp1,
        "highTemp1": highTemp1,
        "desc1": desc1,
        "lowTemp2": lowTemp2,
        "highTemp2": highTemp2,
        "desc2": desc2,
        "lowTemp3": lowTemp3,
        "highTemp3": highTemp3,
        "desc3": desc3,
    }
    return render(request, "weatherInfo/weatherInfo.html", context)



    # return HttpResponse("Hello, world. You're at the polls index.")