# serializers.py
from rest_framework import serializers , viewsets
from .models import CustomUser , CarDriver , CarReservation , Locations
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])

    class Meta:
        model = CustomUser
        fields = ('id','username','prefix','first_name','last_name','email','password1','password2','role')

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password":"Password fields didn't match"})
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        password = validated_data.pop('password1')
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id','username','prefix','first_name','last_name','email','role')

        
class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ('id','name')
        
class CarDriverSerializer(serializers.ModelSerializer):

    startRoute = serializers.StringRelatedField()
    endRoute = serializers.StringRelatedField()
    driver = serializers.StringRelatedField()
    
    
    class Meta:
        model = CarDriver
        fields = ('id','car_number','driver','number_of_seat', 'price_per_unit','is_available','startRoute','endRoute','date','time')
        
        

class CarDriverListSerializer(serializers.ModelSerializer):
        
    startRoute = serializers.PrimaryKeyRelatedField(queryset=Locations.objects.all(),source='startRoute.name')
    endRoute = serializers.PrimaryKeyRelatedField(queryset=Locations.objects.all(),source='endRoute.name')
    
    driver = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(),source='driver.username')
    
    class Meta:
        model = CarDriver
        fields = ('id','car_number','driver','number_of_seat', 'price_per_unit','is_available','startRoute','endRoute','date','time')
        


class ResponseDriverCarSerializer(serializers.ModelSerializer):
   
    startRoute = serializers.PrimaryKeyRelatedField(queryset=Locations.objects.all(),source='startRoute.name')
    endRoute = serializers.PrimaryKeyRelatedField(queryset=Locations.objects.all(),source='endRoute.name')
    
    class Meta:
        model = CarDriver
        fields = ('car_number','startRoute','endRoute','date','time')


       
class CarReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarReservation
        fields = ('number_of_ticket', 'user', 'car', 'number_of_seat', 'is_confirmed' )
        read_only_fields = ('number_of_ticket', 'user')

        
class CarReservationListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(),source='user.username')
    car = serializers.PrimaryKeyRelatedField(queryset=CarDriver.objects.all(),source='car.car_number') 
    class Meta:
        model = CarReservation
        fields = ('id','number_of_ticket', 'user', 'car', 'number_of_seat', 'is_confirmed' , 'amont_to_pay')
               
