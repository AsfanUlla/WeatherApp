from django.conf.urls import url 
from openweatherapi import views
 
urlpatterns = [
    url(r'^weather$', views.weather_data),
]
