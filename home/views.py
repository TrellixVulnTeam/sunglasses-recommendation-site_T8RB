from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Image
from .forms import ImageForm
# Create your views here.
def index(request):
	context = {}
	return render(request, 'home/templates/index.html', context)


def image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

    else:
        form = Image()
    return render(request, 'index.html', {'form': form})


