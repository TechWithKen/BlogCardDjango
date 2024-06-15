from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "cardapp/index.html")

def allcards(request, name):
    return HttpResponse(f"This is the {name.upper()} color card for the Application")


