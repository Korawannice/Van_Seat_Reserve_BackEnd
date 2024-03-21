# serializers.py
from rest_framework import serializers , viewsets
from .models import CustomUser , VanDriver , VanReservation , Locations
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
        
class VanDriverSerializer(serializers.ModelSerializer):

    startRoute = serializers.StringRelatedField()
    endRoute = serializers.StringRelatedField()
    driver = serializers.StringRelatedField()
    
    
    class Meta:
        model = VanDriver
        fields = ('id','van_number','driver','number_of_seat', 'price_per_unit','is_available','startRoute','endRoute','date','time')
        
        

class VanDriverListSerializer(serializers.ModelSerializer):
        
    startRoute = serializers.PrimaryKeyRelatedField(queryset=Locations.objects.all(),source='startRoute.name')
    endRoute = serializers.PrimaryKeyRelatedField(queryset=Locations.objects.all(),source='endRoute.name')
    
    driver = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(),source='driver.username')
    
    class Meta:
        model = VanDriver
        fields = ('id','van_number','driver','number_of_seat', 'price_per_unit','is_available','startRoute','endRoute','date','time')
        


class ResponseDriverCarSerializer(serializers.ModelSerializer):
   
    startRoute = serializers.PrimaryKeyRelatedField(queryset=Locations.objects.all(),source='startRoute.name')
    endRoute = serializers.PrimaryKeyRelatedField(queryset=Locations.objects.all(),source='endRoute.name')
    
    class Meta:
        model = VanDriver
        fields = ('van_number','startRoute','endRoute','date','time')


       
class VanReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VanReservation
        fields = ('number_of_ticket', 'user', 'van', 'number_of_seat', 'is_confirmed' )
        read_only_fields = ('number_of_ticket', 'user')

        
class VanReservationListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(),source='user.username')
    van = serializers.PrimaryKeyRelatedField(queryset=VanDriver.objects.all(),source='van.van_number') 
    class Meta:
        model = VanReservation
        fields = ('id','number_of_ticket', 'user', 'van', 'number_of_seat', 'is_confirmed' , 'amount_to_pay')
               
