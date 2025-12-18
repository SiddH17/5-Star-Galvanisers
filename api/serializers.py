from rest_framework import serializers
from .models import *

from django.contrib.auth.hashers import make_password

#Serializer for Login method
class RegisterSeralizer(serializers.ModelSerializer):
    class Meta:
        model = LoginUsers
        fields = '__all__'

    def validate(self, data):
        if data['email']:
            if LoginUsers.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError({'message': 'Email is already taken'})
            
        return data
    
    def create(self, validated_data):
        user = LoginUsers.objects.create(
            fullname = validated_data['fullname'],
            email = validated_data['email'],
            password = make_password(validated_data['password'])
        )

        user.save()
        print(user)

        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginUsers
        fields = ['email', 'password']

    #Validate the data
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if not email:
            raise serializers.ValidationError({'email': 'Email ID is incorrect.'})
        if not password:
            raise serializers.ValidationError({'password': 'Incorrect Password.'})
        
        return data
