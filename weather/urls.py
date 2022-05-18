#url for weather app
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('weathercheck.urls')) #adding urls from weathercheckup
]

