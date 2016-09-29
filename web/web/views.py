import os
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def home(request):
    # template = loader.get_template('base.html')
    return render(request, 'base.html')
