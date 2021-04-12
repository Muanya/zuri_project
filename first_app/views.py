from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(req):
	return HttpResponse('Hello World! Welcome to the home page.')

def index(req):
	return HttpResponse('Hello World! You are first_app index.')
