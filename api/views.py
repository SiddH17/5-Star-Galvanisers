from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def register_api(request):
    data = request.data
    serializer = RegisterSeralizer(data=data)

    if not serializer.is_valid():
        print('Serializer is not valid', serializer.data)
        return Response({
            'status': '400',
            'message': 'Error while creating user, please try again.',
            'error': serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST)
    
    serializer.save()
    print(serializer.data, "Correct serializer data")
    return Response({
        'status': '201',
        'message': 'User successfully created'
    },
    status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login_api(request):
    data = request.data
    serializer = LoginSerializer(data=data)
    print(data, "The data being received")

    if not serializer.is_valid(): 
        print("Sorry, can't validate the data in the serializer")   
        return Response({
            'status': '400',
            'message': 'Invalid Credentials, please try again.',
        },
        status=status.HTTP_400_BAD_REQUEST)
    
    print("Serializer looks fine here....")
    
    email = serializer.validated_data['email']
    password = serializer.validated_data['password']

    user = LoginUsers.objects.filter(email=email).first()
    print(user)

    #If either user does not exist or user's password does not match
    #check_password(encoded password, original password)
    if not user or not check_password(password, user.password):
        print("Unable to login to the system")
        return Response({
            'status': '401', 
            'message': 'Authentication failed. Please check your email and password.'
            }, 
            status=status.HTTP_401_UNAUTHORIZED)
    
    token = f"{user.id}_{user.username}_{user.password}"
    print(token)

    return Response({
        'status': '200',
        'message': 'Login Successful',
        'token': token
    },
    status=status.HTTP_200_OK)