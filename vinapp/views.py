from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello i am shivam")

# Create your views here.
