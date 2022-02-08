from rest_framework import serializers
from .models import Lectures, User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'phone')
        

class LectureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lectures
        fields = '__all__'