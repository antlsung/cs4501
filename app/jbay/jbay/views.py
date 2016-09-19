from jbay.models import shoes, user
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.http import Http404,HttpResponse
from rest_framework import authentication, permissions
from jbay.serializers import ShoeSerializer, UserSerializer


class ShoeViewSet(generics.ListCreateAPIView):
    queryset = shoes.objects.all()
    serializer_class = ShoeSerializer


class UserViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = user.objects.all()
    serializer_class = UserSerializer

# class ListShoes(APIView):
#
#         def get(self):
#             return  Response('Hello, World!')
# class ShoeView(APIView):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     def get(self, request):
#         # users = User.objects.all()
#         # serializer = UserSerializer(users, many=True)
#         shoe_list = shoes.objects.all()
#         serializer= ShoeSerializer(shoe_list,many=True)
#         return Response(serializer.data)
#


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = user.objects.all()
#     serializer_class = UserSerializer
