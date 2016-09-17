from jbay.models import shoes, user
from rest_framework import serializers


class ShoeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = shoes
        fields = ('shoe', 'brand', 'text', 'created_date','published_date')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ('name', 'address','cart','created_date','published_date')
