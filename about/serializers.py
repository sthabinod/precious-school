from rest_framework import serializers
from .models import About, AdministrativeBody, AdvisoryBoard, BoardOfDirector, History, Message, ServicesAndFacilities

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
    
    
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class BODSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardOfDirector
        fields = '__all__'


class AdminBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrativeBody
        fields = '__all__'


class AdvisoryBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvisoryBoard
        fields = '__all__'
        

class ServicesAndFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesAndFacilities
        fields = '__all__'



    