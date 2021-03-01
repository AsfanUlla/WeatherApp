from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
import requests
import json
import pathlib

# Create your views here.

@api_view(['GET', 'POST'])
def weather_data(request):
    if request.method == 'GET':
        f = open('%s/citylist/city.list.min.json'%(pathlib.Path(__file__).parent.absolute()),)
        names = json.load(f)
        name_list = list()
        for i in names:
            name_list.append({
                "id": i["id"],
                "name": i["name"],
            })
        return render(request, "index2.html", {"name_list": name_list})
        
    if request.method == 'POST':
        city = JSONParser().parse(request)
        weatherdata = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&units=metric&appid=9f6d8e545732cc08df858a6aaffcba92'%(city["city_name"]))
        return JsonResponse(weatherdata.json(), safe=False)