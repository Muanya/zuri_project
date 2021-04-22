from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(req):
	return render(req,'index.html', {'title': 'Home'})

def index(req):
	contxt = {'title': 'First app'}
	return render(req, 'first_app/index.html', contxt)
