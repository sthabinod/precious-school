from django.shortcuts import get_object_or_404, render
import jwt
from rest_framework import generics, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Event,News
from .serializer import CreateEventSerializer, DetailEventSerailizer, CreateNewsSerializer,DetailNewsSerailizer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class EventList(generics.GenericAPIView):
    serializer_class = CreateEventSerializer
    queryset =Event
    permission_classes=[]
    
    @extend_schema(
        operation_id="Get all events",
        description="List all events ",
        request=CreateEventSerializer,
    )
    def get(self,request):
        course =Event.objects.all()
        serializer = self.serializer_class(instance=course,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class CreateEvent(generics.GenericAPIView):
    serializer_class = CreateEventSerializer
    permission_classes=[]
    @extend_schema(
        operation_id="Create events",
        description="Create events ",
        request=CreateEventSerializer,
    )
    def post(self,request):
        print("I am here  2")

        data = request.data
        serializer=self.serializer_class(data=data)
        print("I am here 3")

        if serializer.is_valid():
            print("I am here 4")
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        print("I am here5")
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EventDetailView(generics.GenericAPIView):
    serializer_class = DetailEventSerailizer

    permission_classes=[]
    @extend_schema(
        operation_id="Get Event as per id",
        description="as per id",
        request=CreateEventSerializer,
    )
    def get(self,request,id):
        course = get_object_or_404(Event,pk=id)
        serializer = self.serializer_class(instance=course)
        return Response(data=serializer.data,status = status.HTTP_200_OK)

    @extend_schema(
        operation_id="Update event",
        description="Update event",
        request=CreateEventSerializer,
    )
    def patch(self,request,id):
        data=request.data
        event = get_object_or_404(Event,pk=id)
        serializer = self.serializer_class(data=data,instance=event)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    @extend_schema(
        operation_id="Delete event",
        description="Delete event",
        request=CreateEventSerializer,
    )
    def delete(self,request,id):
        event = Event.objects.filter(id=id)
        event.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)




class NewsList(generics.GenericAPIView):
    serializer_class = CreateNewsSerializer
    queryset =News
    permission_classes=[]
    

    @extend_schema(
        operation_id="Get all news",
        description="List all news ",
        request=CreateEventSerializer,
    )
    def get(self,request):
        news =News.objects.all()
        serializer = self.serializer_class(instance=news,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class CreateNews(generics.GenericAPIView):
    serializer_class = CreateNewsSerializer
    permission_classes=[]

    @extend_schema(
        operation_id="Create a news",
        description="Create a news",
        request=CreateEventSerializer,
    )
    def post(self,request):
        print("I am here  2")

        data = request.data
        serializer=self.serializer_class(data=data)
        print("I am here 3")

        if serializer.is_valid():
            print("I am here 4")
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        print("I am here5")
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class NewsDetailView(generics.GenericAPIView):
    serializer_class = DetailNewsSerailizer
    permission_classes=[]


    @extend_schema(
        operation_id="Get news as per id",
        description="Get news as per id",
        request=CreateEventSerializer,
    )
    def get(self,request,id):
        course = get_object_or_404(News,pk=id)
        serializer = self.serializer_class(instance=course)
        return Response(data=serializer.data,status = status.HTTP_200_OK)

    
    @extend_schema(
        operation_id="Update news",
        description="Update news",
        request=CreateEventSerializer,
    )
    def patch(self,request,id):
        data=request.data
        event = get_object_or_404(News,pk=id)
        serializer = self.serializer_class(data=data,instance=event)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    @extend_schema(
        operation_id="Delete news",
        description="Delete news",
        request=CreateEventSerializer,
    )
    def delete(self,request,id):
        event = Event.objects.filter(id=id)
        event.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
