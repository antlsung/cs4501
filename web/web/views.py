import os
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def show_shoes(request):
	if request.method == 'GET':
		return render(request, 'show_shoes.html')