import requests
from django.http import JsonResponse
import urllib.request
import urllib.parse
import json

def home_list(request):
    if request.method == 'GET':
        resp = requests.get('http://models-api:8000/shoes')
        home_list = resp.json()
        return JsonResponse(home_list,safe=False)

def most_recent(request):
    if request.method == 'GET':
        resp = requests.get('http://models-api:8000/get_shoes?published_date=0')
        recent_list = resp.json()
        return JsonResponse(recent_list,safe=False)



def item_detail(request):
    if request.method == 'GET':
        id_num = request.GET['id']
        # brand = request.GET['brand']
        params = {'id': id_num}
        r = requests.get('http://models-api:8000/get_shoes',params=params)
        shoe_detail = r.json()
        return JsonResponse(shoe_detail)

def create_user(request):
    if request.method == 'POST':
        # req = request.POST
        # id_num = request.POST['id']
        # brand = request.GET['brand']
        # params = {'id': id_num}
        r = requests.post('http://models-api:8000/add_users/',data=request.POST)
        user_detail = r.json()
        return JsonResponse(user_detail)

def create_shoe(request):
    if request.method == 'POST':
        # req = request.POST
        # id_num = request.POST['id']
        # brand = request.GET['brand']
        # params = {'id': id_num}
        r = requests.post('http://models-api:8000/add_shoes/',data=request.POST)
        shoe_detail = r.json()
        return JsonResponse(shoe_detail)
