from rest_framework import serializers
from .models import *


class UserSerializer (serializers.ModelSerializer):
    class Meta :
        model = User
        fields = '__all__'


class ProductSerializer (serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = '__all__'


class CartSerializer (serializers.ModelSerializer):
    class Meta :
        model = Cart
        fields = '__all__'


class Cart_itemSerializer (serializers.ModelSerializer):
    class Meta :
        model = Cart_item
        fields = '__all__'


class CartSerializer (serializers.ModelSerializer):
    class Meta :
        model = Cart
        fields = '__all__'

                
class CategorySerializer (serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = '__all__'