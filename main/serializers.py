from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=120, min_length=3)
    password = serializers.CharField(required=True, min_length=8, max_length=16)

    def validate(self, data):
        if User.objects.filter(username=data.get("username")).count() > 0:
            raise serializers.ValidationError(
                "Пользователь с таким логином уже есть, поменяйте логин"
            )
        return data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=120, min_length=3)
    password = serializers.CharField(required=True, min_length=8, max_length=16)

    def validate(self, data):
        if not User.objects.filter(username=data.get("username")).exists():
            raise serializers.ValidationError("Такого пользователя нет")

        user = User.objects.filter(username=data.get("username")).first()
        if not user.check_password(data.get("password")):
            raise serializers.ValidationError("Неверный пароль")

        return data
