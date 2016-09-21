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




class UserViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = user.objects.all()
    serializer_class = UserSerializer
