from django.urls import path
from . import views

urlpatterns = [
	path('', views.list, name='blog'), # url đến function index trong views
	path('<int:id>', views.post, name='post'),
]