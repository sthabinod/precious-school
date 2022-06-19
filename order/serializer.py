from dataclasses import field
from .models import Event, News
from rest_framework import serializers

class CreateEventSerializer(serializers.ModelSerializer):
    print("I am here 5")
    class Meta:
        model = Event
        fields='__all__'


class DetailEventSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields='__all__'


class CreateNewsSerializer(serializers.ModelSerializer):
    print("I am here 5")
    class Meta:
        model = News
        fields='__all__'


class DetailNewsSerailizer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields='__all__'

