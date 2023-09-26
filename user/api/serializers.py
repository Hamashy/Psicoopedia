from rest_framework import serializers
from user.models import UserUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUser
        fields = ['id', 'email', 'username', 'last_name', 'password']

