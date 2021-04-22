from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(req):
	return render(req,'index.html', {'title': 'Home'})

def index(req):
	return HttpResponse('Hello World! You are first_app index.')
