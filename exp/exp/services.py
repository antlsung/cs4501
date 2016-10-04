import requests
from django.http import JsonResponse

def item_detail(request):
    if request.method == 'GET':
        id_num = request.GET['id']
        # brand = request.GET['brand']
        params = {'id': id_num}
        r = requests.get('http://models-api:8000/get_shoes',params=params)
        shoe_detail = r.json()
        return JsonResponse(shoe_detail)
