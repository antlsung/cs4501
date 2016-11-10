import requests
from django.http import JsonResponse
import urllib.request
import urllib.parse
import json
from django.http import HttpResponse
from kafka import KafkaProducer
from elasticsearch import Elasticsearch

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
        r = requests.get('http://models-api:8000/get_shoes', params=params)
        try:
            shoe_detail = r.json()
            return JsonResponse(shoe_detail)
        except:
            return HttpResponse(r,status=r.status_code)

def user_detail(request):
    if request.method == 'GET':
        id_num = request.GET['id']
        # brand = request.GET['brand']
        params = {'id': id_num}
        r = requests.get('http://models-api:8000/get_users',params=params)
        try:
            user_detail = r.json()
            return JsonResponse(user_detail)
        except:
            return HttpResponse(r,status=r.status_code)

def delete_shoe(request):
    if request.method == 'POST':
        r = requests.post('http://models-api:8000/delete_shoes/',data=request.POST)
        shoe_status = r.status_code
        return HttpResponse(shoe_status)

def delete_user(request):
    if request.method == 'POST':
        r = requests.post('http://models-api:8000/delete_users/',data=request.POST)
        user_status = r.status_code
        return HttpResponse(user_status)

def create_user(request):
    if request.method == 'POST':
        r = requests.post('http://models-api:8000/add_users/',data=request.POST)
        user_detail = r.json()
        return JsonResponse(user_detail)

def create_shoe(request):
    if request.method == 'POST':

        #tell model layer to create shoe
        r = requests.post('http://models-api:8000/add_shoes/',data=request.POST)
        try:
            shoe_detail = r.json()

            # Send to kafka
            producer = KafkaProducer(bootstrap_servers='kafka:9092')
            shoe_new_listing = shoe_detail
            producer.send('shoe-listings', json.dumps(shoe_new_listing).encode('utf-8'))
            return JsonResponse(shoe_detail)
        except:
            return HttpResponse(r)


def login(request):
    if request.method == 'POST':
        # return HttpResponse("exp layer")
        authenticator = requests.post('http://models-api:8000/check_password/', data=request.POST)
        # authenticator = r.json()
        return HttpResponse(authenticator)

def logout(request):
    if request.method == 'POST':
        r = requests.post('http://models-api:8000/logout/',data=request.POST)
        return HttpResponse(r,status=r.status_code)

def logged_in(request):
    if request.method == 'POST':
        r = requests.post('http://models-api:8000/logged_in/', data=request.POST)
        return JsonResponse(r.json())

        # return HttpResponse(r,status=r.status_code)

def search(request):
    if request.method == 'GET':
        # r = requests.post('http://models-api:8000/logged_in/', data=request.POST)
        es = Elasticsearch(['es'])
        keywords = request.GET['keywords']

        results = es.search(index='listing_index', body={'query': {'query_string': {'query':keywords}}, 'size': 10})
        return JsonResponse(results)
        # return JsonResponse({'shoe':'air max'})
