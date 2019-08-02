from django.contrib import admin
from django.urls import path
import log.views


urlpatterns = [
    path('home', log.views.home, name='home'),
]