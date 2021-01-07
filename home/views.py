from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .forms import ImageForm
# Create your views here.
def index(request):
	context = {}
	return render(request, 'home/templates/index.html', context)

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})