from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
# Create your views here.
def index(request):
	context = {}
	return render(request, 'home/templates/index.html', context)