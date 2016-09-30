import os
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def home(request):
    test="hi"
    shoeList=['Curry 1','NB 996','Jordan 12']
    return render(request, 'welcome.html',{'shoeList':shoeList,'test':test})

def show_shoes(request):
	if request.method == 'GET':
		return render(request, 'show_shoes.html')
