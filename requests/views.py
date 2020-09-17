from django.shortcuts import render
from django.http import HttpResponse
from .models import Request

def index(request):
    return HttpResponse("Welcome to the requests page.")
