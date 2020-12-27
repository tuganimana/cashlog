
from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.core.mail import send_mail
import random,os
from random import randint
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields=('__all__')
    
    def create(self,validated_data):
        insert=CustomUser.objects.create_user(
        fullname=validated_data['fullname'],
        telephone=validated_data['telephone'],
        password=make_password(validated_data['password']),
        accounttype='users'
        
        )
        email=validated_data['email']
        # subject='Verification from City Plus'
        # message='This link is for activating your account on city plus \n'+'your Username:  '+email+'\n https://www.cityplus.rw/activation/'+email+'/'
        # from_email=settings.EMAIL_HOST_USER
        # rt=send_mail(subject,message,from_email,[str(email),],fail_silently=False)
       
        return insert
