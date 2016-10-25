from jbay.models import users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view
from django.contrib.auth import hashers
from django.http import Http404,HttpResponse
from rest_framework import authentication, permissions
from jbay.serializers import UserSerializer
import os
import hmac
import settings

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        queryset = users.objects.all()
        serializer_class = UserSerializer
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def get_users(request):
    if request.method == 'GET':
        # get_id = request.GET['id']
        # data = request.GET
        # serializer = UserSerializer(users.objects.get(id=get_id))
        # return Response(serializer.data, status=status.HTTP_200_OK)
        params = request.GET
        if 'id' in params:
            get_id = request.GET['id']
            serializer = UserSerializer(users.objects.get(id=get_id))
            return Response(serializer.data, status=status.HTTP_200_OK)
        if 'name' in params:
            get_name = request.GET['name']
            serializer = UserSerializer(users.objects.filter(name=get_name),many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response("Invalid Request",status=status.HTTP_400_BAD_REQUEST)

#add multiple users at a time, for later, then change url to add_users
@api_view(['GET','POST'])
def add_users(request):

    hash_pass = hashers.make_password(request.data['password'])
    request.data['password'] = hash_pass
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response("Invalid Request",status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def update_users(request):
    if request.method == 'POST':
        post_id = request.POST['id']
        data = request.POST
        serializer = UserSerializer(users.objects.get(id=post_id),data=data, partial=True)
        if (serializer.is_valid()):
            shoe = users.objects.get(pk=post_id)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response("Invalid Request",status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def delete_users(request):
    if request.method == 'POST':
        post_id = request.POST['id']
        delete_user = users.objects.get(id=post_id)
        deleted = delete_user
        delete_user.delete()
        return Response("User: "+str(deleted.name) +" (ID: #"+ str(post_id) + ") has been deleted")
    return Response("Invalid Request",status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def check_password(request):
    if request.method == 'POST':
        # return HttpResponse("in models layer check_password func")
        post_username = request.POST['username']
        post_password = request.POST['password']
        user = users.objects.get(name=post_username)
        hash_pass = hashers.make_password(post_password)
        # return HttpResponse(user.password + " " + hash_pass)
        if user.password == post_password:
            authenticator = hmac.new(key=settings.SECRET_KEY.encode('utf-8'), msg=os.urandom(32),
                                     digestmod='sha256').hexdigest()
            return authenticator
