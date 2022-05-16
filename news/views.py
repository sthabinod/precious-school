from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import NewsSerializer
from .models import News

class NewsView(APIView):
    def get(self, request,format=None):
        query = News.objects.all()
        serializer = NewsSerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def post(self,request,format=None):
        serializer = NewsSerializer(data = request.data)
        print("Here")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
    