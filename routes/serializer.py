from rest_framework import serializers
from .models import  Routes, AddRoutes
from user.models import User
from user.serializer import UserSerializer

class RoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'
        dept = 2
         
class AddRoutesSerializer(serializers.ModelSerializer):
    startRoute = serializers.PrimaryKeyRelatedField(
        queryset=Routes.objects.all(),
        required=True 
    )
    endRoute = serializers.PrimaryKeyRelatedField(
        queryset=Routes.objects.all(),
        required=True      
    )
    driver = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=True      
    )
    startRoute_id = RoutesSerializer(source='startRoute', read_only=True)
    endRoute_id = RoutesSerializer(source='endRoute', read_only=True)
    driver_id = UserSerializer(source='driver', read_only=True)
    
    class Meta:
        model = AddRoutes
        fields = '__all__'
        dept = 2
        
        
