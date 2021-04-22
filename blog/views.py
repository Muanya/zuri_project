from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
	contxt = {'title': 'Blog'}
	return render(req, 'blog/index.html', contxt)