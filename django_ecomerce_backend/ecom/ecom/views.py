from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status, permissions


class signup(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def post(self, request):
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        username = request.data['username']
        password = request.data['password']

        if User.objects.filter(username=username).exists():
            return HttpResponse('User Exists')
        elif User.objects.filter(email=email).exists():
            return HttpResponse('User with the email id already exists')

        else:
            user = User(username=username, first_name=first_name,
                        last_name=last_name, email=email)
            user.set_password(password)
            user.save()
            data = UserSerializer(user)
            return Response(data.data, status=status.HTTP_201_CREATED)
