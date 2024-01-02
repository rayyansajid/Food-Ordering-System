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

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'name')

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'date', 'status', 'totalamount', 'paymethod', 'rating', 'review', 'customer')

class FlavorCatSerializer(serializers.ModelSerializer):
    flavor = FlavorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = FlavorCat
        fields = ('id', 'flavor', 'category')

class WishlistSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    dessert = DessertSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = ('id', 'customer', 'dessert')

class CatalogItemSerializer(serializers.ModelSerializer):
    dessert = DessertSerializer(read_only=True)
    unit = UnitSerializer(read_only=True)

    class Meta:
        model = CatalogItem
        fields = ('id', 'dessert', 'unit', 'price')

class CustomerCartSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = CustomerCart
        fields = ('id', 'customer')

class CartItemSerializer(serializers.ModelSerializer):
    catalogitem = CatalogItemSerializer(read_only=True)
    cart = CustomerCartSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ('id', 'catalogitem', 'cart', 'quantity')

class OrderItemSerializer(serializers.ModelSerializer):
    catalogitem = CatalogItemSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'catalogitem', 'order', 'quantity')

