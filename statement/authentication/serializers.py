from rest_framework import serializers
from .models import CustomUser


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email',
                  'password', 'role']


class UsersListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'role']
