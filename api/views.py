from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from django.http import JsonResponse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

def welcome(request):
    return HttpResponse('Welcome Idapay ') 

@csrf_exempt
def accountcreation(request):
    if request.method=='GET':
        reg=CustomUser.objects.all()
        serializer=UserSerializer(reg,many=True)
        return JsonResponse(serializer.data,safe=False)
        
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'account create successful'},status=201)
        return JsonResponse(serializer.errors,status=400)

