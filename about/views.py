from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import AboutSerializer, AdvisoryBoardSerializer, BODSerializer, HistorySerializer, MessageSerializer,AdminBodySerializer, ServicesAndFacilitiesSerializer
from .models import About, AdministrativeBody, AdvisoryBoard, BoardOfDirector,Message,History


class AboutView(APIView):
    def get(self, request,format=None):
        query = About.objects.all()
        serializer = AboutSerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
                            
    def post(self,request,format=None):
        serializer = AboutSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class MessageView(APIView):
    def get(self, request,format=None):
        query = Message.objects.all()
        serializer = MessageSerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
                            
    def post(self,request,format=None):
        serializer = MessageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class HistoryView(APIView):
    def get(self, request,format=None):
        query = History.objects.all()
        serializer = HistorySerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
                            
    def post(self,request,format=None):
        serializer = HistorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    

class BODView(APIView):
    def get(self, request,format=None):
        query = BoardOfDirector.objects.all()
        serializer = BODSerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
                            
    def post(self,request,format=None):
        serializer = BODSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class AdminBodyView(APIView):
    def get(self, request,format=None):
        query = AdministrativeBody.objects.all()
        serializer = AdminBodySerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
                            
    def post(self,request,format=None):
        serializer = AdminBodySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    

class AdviseBodyView(APIView):
    def get(self, request,format=None):
        query = AdvisoryBoard.objects.all()
        serializer = AdvisoryBoardSerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
                            
    def post(self,request,format=None):
        serializer = AdvisoryBoardSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ServiceView(APIView):
    def get(self, request,format=None):
        query = AdvisoryBoard.objects.all()
        serializer = ServicesAndFacilitiesSerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
                            
    def post(self,request,format=None):
        serializer = ServicesAndFacilitiesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)