from django.urls import path
from . import views

urlpatterns = [
	path('', views.index), # url đến function index trong views
	path('contact/', views.contact, name='contact'),
]