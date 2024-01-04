from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'username', 'password', 'name', 'contact', 'email', 'address')
        extra_kwargs = {'password': {'write_only': True}}  # Make password write-only

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class FlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = ('id', 'name')

class DessertSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    flavor = FlavorSerializer(read_only=True)

    class Meta:
        model = Dessert
        fields = ('id', 'name', 'stockquantity', 'description', 'category', 'flavor')

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['category']=CategorySerializer(instance.category).data
        response['flavor']=FlavorSerializer(instance.flavor).data
        return response

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'date', 'status', 'totalamount', 'paymethod', 'rating', 'review', 'customer')

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['customer']=CustomerSerializer(instance.customer).data
        return response

class FlavorCatSerializer(serializers.ModelSerializer):
    flavor = FlavorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = FlavorCat
        fields = ('id', 'flavor', 'category')

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['flavor'] = FlavorSerializer(instance.flavor).data
        response['category']=CategorySerializer(instance.category).data
        return response

class WishlistSerializer(serializers.ModelSerializer):
#     Payload of json should be:
#     {
#     "customer_id": 1,
#     "dessert_ids": [2, 3, 4]
#   }

    customer = CustomerSerializer(read_only=True)
    dessert = DessertSerializer(many=True, read_only=True)

    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(),
        source='customer',
        write_only=True
    )
    dessert_ids = serializers.PrimaryKeyRelatedField(
        queryset=Dessert.objects.all(),
        source='dessert',
        many=True,
        write_only=True
    )

    class Meta:
        model = Wishlist
        fields = ('id', 'customer_id', 'dessert_ids')

    def create(self, validated_data):
        desserts_data = validated_data.pop('dessert', [])
        wishlist = Wishlist.objects.create(**validated_data)
        wishlist.dessert.set(desserts_data)
        return wishlist

    def update(self, instance, validated_data):
        if 'dessert' in validated_data:
            instance.dessert.set(validated_data['dessert'])
        return instance


class CustomerCartSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = CustomerCart
        fields = ('id', 'customer')

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['customer']=CustomerSerializer(instance.customer).data
        return response

class CartItemSerializer(serializers.ModelSerializer):
    dessert = DessertSerializer(read_only=True)
    cart = CustomerCartSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ('id', 'dessert', 'cart', 'quantity')

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['dessert'] = DessertSerializer(instance.dessert).data
        response['cart']=CategorySerializer(instance.cart).data
        return response

class OrderItemSerializer(serializers.ModelSerializer):
    dessert = DessertSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'dessert', 'order', 'quantity')
    
    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['dessert'] = DessertSerializer(instance.dessert).data
        response['order']=CategorySerializer(instance.order).data
        return response

