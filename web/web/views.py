import os
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def home(request):
    return render(request, 'welcome.html')

def show_shoes(request):
	if request.method == 'GET':
		r = requests.get('http://localhost:8001/shoes')
		return render(request, 'show_shoes.html')
