from django.shortcuts import render
from http.client import HTTPResponse

# Create your views here.


def home(request):
    return HTTPResponse("here ia mm")