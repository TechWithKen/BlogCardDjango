from . import views
from django.urls import path

urlspattern = [
    path('', views.home, name="home"),
    path('<str:name>', views.allcards, name="allcards"),
]