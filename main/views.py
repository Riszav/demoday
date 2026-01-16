from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.serializers import LoginSerializer, RegisterSerializer


@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = User.objects.create_user(**serializer.validated_data)
        user.save()
        return Response({"Регистрация прошла успешно"})

    return Response({"Регистрация не удалась"})


@api_view(["POST"])
def login(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        return Response({"Вы успешно вошли!"})

    return Response({"Вход не удался"})
