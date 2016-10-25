from jbay.models import shoes, users, Authenticator
from rest_framework import serializers


class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = shoes
        fields = ('id', 'shoe', 'brand', 'text', 'created_date','published_date')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ('id','name', 'address','password','cart','created_date','published_date')

class AuthenticatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authenticator
        fields = ('authenticator', 'user_id')