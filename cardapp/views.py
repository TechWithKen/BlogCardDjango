from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This the the Home for the Card")

def allcards(request, name):
    return HttpResponse(f"This is the {name} color card for the Application")


