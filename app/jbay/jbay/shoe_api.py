from jbay.models import shoes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view

from django.http import Http404,HttpResponse, QueryDict
from rest_framework import authentication, permissions
from jbay.serializers import ShoeSerializer
import json


@api_view(['GET', 'POST'])
def shoe_list(request):
    if request.method == 'GET':
        queryset = shoes.objects.all()
        serializer_class = ShoeSerializer
        serializer = ShoeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def get_shoes(request):
    if request.method == 'GET':
        params = request.GET
        if 'id' in params:
            get_id = request.GET['id']
            serializer = ShoeSerializer(shoes.objects.get(id=get_id))
            return Response(serializer.data, status=status.HTTP_200_OK)
        if 'brand' in params:
            get_brand = request.GET['brand']
            serializer = ShoeSerializer(shoes.objects.filter(brand=get_brand),many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if 'published_date' in params:
            get_date = request.GET['published_date']
            serializer = ShoeSerializer(shoes.objects.order_by('-published_date'),many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # if request.GET['id'] != None:
        #     get_id = request.GET['id']
        #     data = request.GET
        #     serializer = ShoeSerializer(shoes.objects.get(id=get_id))
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # if request.GET['brand'] != None:
        #     get_brand = request.GET['brand']
        #     data = request.GET
        #     serializer = ShoeSerializer(shoes.objects.get(brand=get_brand))
            # return Response(serializer.data, status=status.HTTP_200_OK)
    return Response("Invalid Request",status=status.HTTP_400_BAD_REQUEST)

#add multiple shoes at a time, for later, then change url to add_shoes
@api_view(['GET','POST'])
def add_shoes(request):
    if request.method == 'POST':
        serializer = ShoeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response("Invalid Request",status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def update_shoes(request):
    if request.method == 'POST':
        post_id = request.POST['id']
        data = request.POST
        serializer = ShoeSerializer(shoes.objects.get(id=post_id),data=data, partial=True)
        if (serializer.is_valid()):
            shoe = shoes.objects.get(pk=post_id)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response("Invalid Request",status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def delete_shoes(request):
    if request.method == 'POST':
        post_id = request.POST['id']
        delete_shoe = shoes.objects.get(id=post_id)
        deleted = delete_shoe
        delete_shoe.delete()
        return Response("Shoe: "+str(deleted.shoe) +" (ID: #"+ str(post_id) + ") has been deleted",status=status.HTTP_200_OK)
    return Response("Invalid Request",status=status.HTTP_400_BAD_REQUEST)
