from jbay.models import shoes, user
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view

from django.http import Http404,HttpResponse
from rest_framework import authentication, permissions
from jbay.serializers import ShoeSerializer, UserSerializer


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        queryset = user.objects.all()
        serializer_class = UserSerializer
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #  return Response({'received data': request.data})
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST','PUT'])
def update_users(request):
    if request.method == 'POST':

        post_id = request.POST['id']
        data = request.POST
        serializer = UserSerializer(user.objects.get(id=post_id),data=data, partial=True)
        if (serializer.is_valid()):
            shoe = user.objects.get(pk=post_id)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("failed")

@api_view(['GET', 'POST','PUT'])
def delete_users(request):
    if request.method == 'POST':

        post_id = request.POST['id']
        delete_shoe = user.objects.get(id=post_id)
        delete_shoe.delete()
        return Response("done")