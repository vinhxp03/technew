from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import RegistrationFrom

# Create your views here.
def index(request):
	return render(request, 'pages/home.html')
def contact(request):
	return render(request, 'pages/contact.html')
def errors(request):
	return render(request, 'pages/error.html')
def register(request):
	form = RegistrationFrom()
	if request.method == 'POST':
		form = RegistrationFrom(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	return render(request, 'pages/register.html', {'form': form})