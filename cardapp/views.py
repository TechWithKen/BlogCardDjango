from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This the the Home for the Card")

def allcards(name):
    return HttpResponse(f'The is the {name} card for the blog app')

