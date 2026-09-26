from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from rest_framework.response import Response
# Create your views here.
# use this method when not using the rest framework
# @api_view (['GET'])
# def getUsers (requests):
#   users = User.objects.all()
#   serializer = UserSerializer(users,many=True)
#   return Response (serializer.data)

# @api_view (['POST'])
# def createUsers (requests):
#   users = User.objects.all()
#   serializer = UserSerializer(users,many=True)
#   return Response (serializer.data)

class UserViewSet (ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet (ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet (ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CartViewSet (ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class Cart_itemViewSet (ModelViewSet):
    queryset = Cart_item.objects.all()
    serializer_class = Cart_itemSerializer
