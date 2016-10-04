import os
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests

def home(request):
    if request.method == 'GET':
        shoeList = requests.get('http://exp-api:8000/home_list')
        # shoeList=['Curry 1','NB996','Jordan 12']
        return render(request, 'welcome.html',{'shoeList':shoeList.json})
        # return render(request, 'welcome.html',{'shoeList':shoeList,'test':test})

def show_shoes(request):
    if request.method == 'GET':
        id_num = request.GET['id']
        # brand = request.GET['brand']

        params = {'id': id_num}
        shoe = requests.get('http://exp-api:8000/item_detail',params=params)

        # return HttpResponse(shoe)

        return render(request, 'show_shoes.html',{'shoe':shoe.json})
