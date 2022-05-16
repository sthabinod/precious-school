from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ProgramSerializer
from .models import Program

class ProgramView(APIView):
    def get(self, request,format=None):
        query = Program.objects.all()
        serializer = ProgramSerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def post(self,request,format=None):
        serializer = ProgramSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
    