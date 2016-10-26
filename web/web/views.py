import os
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
import requests
import json
from django.contrib.auth import hashers
from .forms import CreateUser,CreateShoe,Login
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie

# import logging

# logger = logging.getLogger("debug log")


def home(request):
    if request.method == 'GET':
        auth = request.COOKIES.get("auth")
        data = {"auth": auth}
        logged_in = requests.post('http://exp-api:8000/logged_in/', data=data)
        login_bool = logged_in.json()

        r = requests.get('http://exp-api:8000/home_list')

        shoe_json = r.json()

        shoe_list = []
        for shoe in shoe_json:
            shoe_list.append(shoe)
        #Ordered by Recent Shoes
        r = requests.get('http://exp-api:8000/most_recent')
        recent_json = r.json()
        recent = []
        for shoe in recent_json:
            recent.append(shoe)
        return render(request, 'welcome.html',{'shoeList':shoe_list,'recent':recent,'login':login_bool})
        # return render(request, 'welcome.html',{'shoeList':shoeList,'test':test})

def show_shoe(request):
    if request.method == 'GET':
        auth = request.COOKIES.get("auth")
        data = {"auth": auth}
        logged_in = requests.post('http://exp-api:8000/logged_in/', data=data)
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
        return render(request, 'show_shoes.html',{'shoe':shoe,'date':date,'time':time,'logged_in':logged_in.content})


def show_user(request):
    if request.method == 'GET':
        auth = request.COOKIES.get("auth")
        data = {"auth": auth}
        logged_in = requests.post('http://exp-api:8000/logged_in/', data=data)

        id_num = request.GET['id']
        # brand = request.GET['brand']

        params = {'id': id_num}
        user_req = requests.get('http://exp-api:8000/user_detail',params=params)
        user = user_req.json()
        # return HttpResponse(shoe)
        return render(request, 'show_user.html',{'user':user,'logged_in':logged_in.content})


@csrf_exempt
def create_user(request):
    if request.method == 'POST':

        auth = request.COOKIES.get("auth")
        data = {"auth": auth}
        logged_in = requests.post('http://exp-api:8000/logged_in/', data=data)

        # create a form instance and populate it with data from the request:
        form = CreateUser(request.POST)
        # check whether it's valid:
        if form.is_valid():
            hash_pass = hashers.make_password(request.POST['password'])
            data = request.POST.copy()
            data['password'] = hash_pass
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            user_req = requests.post('http://exp-api:8000/create_user/',data=data)
            user = user_req.json()

            return render(request, 'created_user.html',{'user':user, 'logged_in':str(logged_in.content)})

            # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateUser(auto_id='%s')

    return render(request, 'user_form.html', {'form': form})

@csrf_exempt
def create_shoe(request):

    auth = request.COOKIES.get("auth")
    data = {"auth": auth}
    logged_in = requests.post('http://exp-api:8000/logged_in/', data=data)
    # return HttpResponse(logged_in)

      # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateShoe(request.POST)
        # check whether it's valid:
        if form.is_valid():
            auth = request.COOKIES.get("auth")
            # return HttpResponse(auth)
            data = request.POST.copy()
            data["auth"] = auth
            shoe_req = requests.post('http://exp-api:8000/create_shoe/',data=data)
            # return HttpResponse(shoe_req)
            shoe = shoe_req.json()
            # hi=json.load(shoe.json())
            date_time = shoe['published_date'].split('T')
            date = date_time[0]
            time = date_time[1]
            # return HttpResponse(shoe)
            return render(request, 'created_shoe.html',{'shoe':shoe,'date':date,'time':time,'logged_in':logged_in})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateShoe(auto_id='%s')

    return render(request, 'shoe_form.html', {'form': form, 'logged_in':logged_in.content})

@csrf_exempt
def login(request):
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = Login(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            authenticator = requests.post('http://exp-api:8000/login/',data=request.POST)
            # user = user_req.json()
            # return HttpResponse(authenticator.text)
            response = render(request, 'login_success.html', {'logged_in':True})
            response.set_cookie("auth",authenticator.content[1:-1])
            # response.set_cookie("ben", "hello")
            return response

            # if a GET (or any other method) we'll create a blank form
    else:
        form = Login(auto_id='%s')

    return render(request, 'login.html', {'form': form,})

@csrf_exempt
def logout(request):
    if request.method == 'GET':
        auth = request.COOKIES.get("auth")
        data={"auth":auth}
        logout = requests.post('http://exp-api:8000/logout/', data=data)
        # return HttpResponse(logout)
        return render(request, 'logout.html',{'logged_in':False})
    else:
        return render(request, 'welcome.html')
