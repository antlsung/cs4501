import os
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests
import json
# import logging

# logger = logging.getLogger("debug log")


def home(request):
    if request.method == 'GET':
        r = requests.get('http://exp-api:8000/home_list')
        # logger.debug(r.json)

        # return HttpResponse(r)
        # print(r.json)
        # return render(request, 'welcome.html',{'shoeList':r})
        # return HttpResponse(r)

        shoe_json = r.json()
        # shoe = shoe_json
        # return HttpResponse(shoe_json)
        shoe_list = []
        for shoe in shoe_json:
            shoe_list.append(shoe)
        # return HttpResponse(shoe_list)
        # shoeList = json.load(r.json())
        # shoes = []
        # for shoe in shoeList:
        #     shoes.append(shoe)
        # return HttpResponse(shoeList)
        # shoeList=['Curry 1','NB996','Jordan 12']

        return render(request, 'welcome.html',{'shoeList':shoe_list})
        # return render(request, 'welcome.html',{'shoeList':shoeList,'test':test})

def show_shoes(request):
    if request.method == 'GET':
        id_num = request.GET['id']
        # brand = request.GET['brand']

        params = {'id': id_num}
        shoe = requests.get('http://exp-api:8000/item_detail',params=params)

        # return HttpResponse(shoe)

        return render(request, 'show_shoes.html',{'shoe':shoe.json})
