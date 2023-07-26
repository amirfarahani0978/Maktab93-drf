from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializers
from django.contrib.auth.models import User
from rest_framework import status


"""
use status code
"""
class UserRegister(APIView):
    def post(self, request):
        #ser_data = UserRegisterSerializers(data = request.POST)
        ser_data = UserRegisterSerializers(data = request.data)
        if ser_data.is_valid():
            # User.objects.create_user(
            #     username = ser_data.validated_data['username'],
            #     password=  ser_data.validated_data['password'],
            #     email = ser_data.validated_data['email']
            # )
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data , status = status.HTTP_201_CREATED)
        return Response(ser_data.errors , status=status.HTTP_400_BAD_REQUEST)