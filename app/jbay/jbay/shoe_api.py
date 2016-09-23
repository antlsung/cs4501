from jbay.models import shoes, user
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view

from django.http import Http404,HttpResponse, QueryDict
from rest_framework import authentication, permissions
from jbay.serializers import ShoeSerializer, UserSerializer
import json


@api_view(['GET', 'POST','PUT'])
def shoe_list(request):
    if request.method == 'GET':
        queryset = shoes.objects.all()
        serializer_class = ShoeSerializer
        serializer = ShoeSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #  return Response({'received data': request.data})
        serializer = ShoeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
    	put = QueryDict(request.body)
    	id = put.get('brand')
    	return Response(request.body)


@api_view(['GET', 'POST','PUT'])
def update_shoes(request):
	if request.method == 'POST':

		post_id = request.POST['id']
		data = request.POST
		serializer = ShoeSerializer(shoes.objects.get(id=post_id),data=data, partial=True)
		if (serializer.is_valid()):
			shoe = shoes.objects.get(pk=post_id)
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)

		return Response("failed")

@api_view(['GET', 'POST','PUT'])
def delete_shoes(request):
	if request.method == 'POST':

		post_id = request.POST['id']
		delete_shoe = shoes.objects.get(id=post_id)
		delete_shoe.delete()
		return Response("done")
