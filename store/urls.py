from django.urls import path
from django.contrib import admin
from . import views

app_name = "store"

urlpatterns = [
    path("", views.home, name="home"),

]