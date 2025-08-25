from django.shortcuts import render
from http.client import HTTPResponse
from django.template.loader import render_to_string
from django.http import HttpResponse

# Create your views here.


def starting_page(request):
   return HttpResponse("Hello, world. You're at the polls page.")


def posts(request):
    return HttpResponse("Returns all the post")


def post_detail(request, slug):
    return HttpResponse(f"this is the slug {slug}")