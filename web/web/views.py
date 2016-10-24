import os
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
import requests
import json
from .forms import CreateUser,CreateShoe
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie

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

        return render(request, 'welcome.html',{'shoeList':shoe_list})
        # return render(request, 'welcome.html',{'shoeList':shoeList,'test':test})

def show_shoes(request):
    if request.method == 'GET':
        id_num = request.GET['id']
        # brand = request.GET['brand']

        params = {'id': id_num}
        shoe_req = requests.get('http://exp-api:8000/item_detail',params=params)
        shoe = shoe_req.json()
        # hi=json.load(shoe.json())
        date_time = shoe['published_date'].split('T')
        date = date_time[0]
        time = date_time[1]
        # return HttpResponse(shoe)
        return render(request, 'show_shoes.html',{'shoe':shoe,'date':date,'time':time})

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateUser(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            user_req = requests.post('http://exp-api:8000/create_user/',data=request.POST)
            user = user_req.json()

            return render(request, 'created_user.html',{'user':user})

            # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateUser(auto_id='%s')

    return render(request, 'user_form.html', {'form': form})

@csrf_exempt
def create_shoe(request):
      # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateShoe(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            shoe_req = requests.post('http://exp-api:8000/create_shoe/',data=request.POST)
            shoe = shoe_req.json()
            # hi=json.load(shoe.json())
            date_time = shoe['published_date'].split('T')
            date = date_time[0]
            time = date_time[1]
            # return HttpResponse(shoe)
            return render(request, 'created_shoe.html',{'shoe':shoe,'date':date,'time':time})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateShoe(auto_id='%s')

    return render(request, 'shoe_form.html', {'form': form})


    # if request.method == 'GET':
    #     form = CreateShoe(auto_id='%s')
    #     return render(request, 'shoe_form.html', {'form': form})
    # return HttpResponse(request.body)
    # shoe_req = requests.post('http://exp-api:8000/create_shoe/',data=request.body)
    # return HttpResponse(shoe_req)


    #     # create a form instance and populate it with data from the request:
    #     # form = CreateShoe(request.POST)
    #     # return HttpResponse(request)
    #
    #     # return HttpResponse(request.body)
    #     # shoe_req = requests.get('http://exp-api:8000/item_detail',params={'id':1})
    #     shoe_req = requests.post('http://exp-api:8000/create_shoe/',data=request.body)
    #     return HttpResponse(shoe_req)
    #
    #     shoe = shoe_req.json()
    #     # hi=json.load(shoe.json())
    #     date_time = shoe['published_date'].split('T')
    #     date = date_time[0]
    #     time = date_time[1]
    #     # return HttpResponse(shoe)
    #     return render(request, 'show_shoes.html',{'shoe':shoe,'date':date,'time':time})
    #
    #
    #
    # else:
