from ast import Pass
from asyncio import current_task
from dataclasses import fields
from lib2to3.pgen2 import token
from xml.dom import ValidationErr
import django
from django.contrib.auth.password_validation import validate_password
from phonenumber_field.serializerfields import PhoneNumberField
from requests import Response, request
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# password reset token geneator
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,smart_bytes,force_str,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode 
from rest_framework.exceptions import AuthenticationFailed
from .models import User


# password reset token geneator
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode 

# send mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util

# importing for generating random password
import random
import string

def generate_random_password():

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols

    temp = random.sample(all,10)

    password = "".join(temp)

    return password




class UserCreationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)
    class Meta:
        # declararing model serializers and setting model meaning for validating as per model
        model = User
        # these fields are visible to the frontend
        fields = ('email','password')

    def validate(self, attrs):
        check_user = User.objects.filter(email=attrs['email']).exists()

        if check_user:
            raise serializers.ValidationError(detail="Email already exists!")
      

        # check_username = User.objects.filter(username=attrs['username']).exists()

        # if check_username:
        #     raise serializers.ValidationError(detail="Username already exists!")
        
        # check_phone = User.objects.filter(mobile_number=attrs['mobile_number']).exists()

        # if check_phone:
        #     raise serializers.ValidationError(detail="Mobile Number already exists!")
        

        # if attrs['password'] != attrs['password_two']:
        #     raise serializers.ValidationError(detail="Password does not match!")



        return super().validate(attrs)

    # validated data can written as **validated_data only takes data from model and validated model
    def create(self,validated_data):
        user = User.objects.create(email=validated_data['email'],username="rasdfndom")
        password = generate_random_password()
        print(password)
        user.set_password(password)
        user.save()
        print(" I am here*  *  ** ** * ** * * ** * * ** * * ** * * ** * * ")
        # current_site = get_current_site(attrs['request']).domain
        user = User.objects.get(email=validated_data['email'])
        print(user.email)
        # absurl = 'http://'+current_site+""
        email_body = 'Hi '+user.email+', use this password '+ str(password) + " for login!"
        data = {'email_body':email_body,'to_email':user.email,'email_subject':'Welcome to Precious School, login details.'}
        Util.send_email(data)
        return User
    


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token


class ResetPasswordSerailizer(serializers.Serializer):
    email = serializers.EmailField(min_length=10)
    class Meta:
        fields=('email')
    
    # def validate(self, attrs):
    #         email=attrs['data'].get('email')
            
    #         return super().validate(attrs)
    

class SetNewPasswordSerailizer(serializers.Serializer):
    password = serializers.CharField(min_length=10,write_only=True)
    token = serializers.CharField(min_length=1,write_only=True)
    uidb = serializers.CharField(min_length=1,write_only=True)

    class Meta:
        fields=['password','token','uidb']


    def validate(self, attrs):
        try:
            password=attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')
            id= force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            print(user)

            if not PasswordResetTokenGenerator().check_token(user,token):
                raise AuthenticationFailed('The reset link in invalid!')
            user.set_password(password)
            user.save() 

        except Exception as e:
            pass
        return super().validate(attrs)