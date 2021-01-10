from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
	path('', views.home, name='home-page'),
	path('scan/', views.scan, name='scan-page'),
]
