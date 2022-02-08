from rest_framework import serializers
from .models import Lectures, Users

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = ('id', 'email', 'name', 'phone')
        

class LectureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lectures
        fields = '__all__'