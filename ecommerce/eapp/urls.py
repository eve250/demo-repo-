from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    'Users',UserViewSet,basename ='users'
)
router.register (
    'Category',CategoryViewSet,basename='category'
)

router.register (
    'Cart',CartViewSet,basename='cart'
)
router.register (
    'Cart_item',Cart_itemViewSet,basename='cart_item'
)
router.register (
    'Product',ProductViewSet,basename='product'
)

urlpatterns = [
    path('',include(router.urls)),
]