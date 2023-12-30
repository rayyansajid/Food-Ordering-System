from rest_framework import serializers
from .models import Customer
class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length = 10)                                
    password = serializers.CharField(max_length = 10)
    name =  serializers.CharField(max_length = 20)
    contact = serializers.CharField(max_length = 10)
    email = serializers.EmailField()
    address = serializers.CharField(max_length = 50)
    
    def create(self, validated_data):
        return Customer.objects.create(**validated_data)
    
class FlavorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length = 10) 

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)
    
class FeedbackSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    rating = serializers.IntegerField()
    review = serializers.CharField(max_length = 10) 
    
    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

class DessertSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length = 10)
    stockquantity = serializers.IntegerField()
    description = serializers.CharField(max_length = 10) 
    #category = 

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)
    
class UnitSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length = 10) 

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    Status = serializers.CharField(max_length = 10) 
    totalamount = serializers.FloatField()
    paymethod = serializers.CharField(max_length = 10)
    
    def create(self, validated_data):
        return Customer.objects.create(**validated_data)