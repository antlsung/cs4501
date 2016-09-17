from jbay.models import shoes, user
from rest_framework import viewsets
from jbay.serializers import ShoeSerializer, UserSerializer


class ShoeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = shoes.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = user.objects.all()
    serializer_class = GroupSerializer
