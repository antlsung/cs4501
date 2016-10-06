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
        # req = urllib.request.Request('http://models-api:8000/shoes')
        # resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        # resp = json.loads(resp_json)
        # print(resp)

def item_detail(request):
    if request.method == 'GET':
        id_num = request.GET['id']
        # brand = request.GET['brand']
        params = {'id': id_num}
        r = requests.get('http://models-api:8000/get_shoes',params=params)
        shoe_detail = r.json()
        return JsonResponse(shoe_detail)
