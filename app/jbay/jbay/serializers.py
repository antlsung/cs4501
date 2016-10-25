from jbay.models import shoes, users
from rest_framework import serializers


class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = shoes
        fields = ('id', 'shoe', 'brand', 'text', 'created_date','published_date')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ('id','name', 'address','password','cart','created_date','published_date')
