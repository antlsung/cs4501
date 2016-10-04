import requests
from django.http import JsonResponse

def home_list(request):
    if request.method == 'GET':
        r = requests.get('http://models-api:8000/shoes')
        home_list = r.json()
        return JsonResponse(home_list)

def item_detail(request):
    if request.method == 'GET':
        id_num = request.GET['id']
        # brand = request.GET['brand']
        params = {'id': id_num}
        r = requests.get('http://models-api:8000/get_shoes',params=params)
        shoe_detail = r.json()
        return JsonResponse(shoe_detail)
