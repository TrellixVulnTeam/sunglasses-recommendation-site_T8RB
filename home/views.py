from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Image
from .forms import ImageForm
# Create your views here.
def home(request):
	context = {}
	return render(request, 'home/templates/home.html', context)


def scan(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

    else:
        form = Image()
    return render(request, 'face-scan.html', {'form': form})


