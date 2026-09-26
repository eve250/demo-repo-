from django.db import models
from django.conf import settings
# Create your models here.


class User ( models.Model ):
    name = models.CharField(50)
    email = models.EmailField(unique=True)
    password = models.CharField(unique=True)
    def __str__(self):
        
        return self.name

class Category (models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)

    def __str__(self):
        
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        
        return self.description
    
class  Cart (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time = models.DateTimeField
    def __str__(self, *args, **kwargs):
            super().__str__(*args, **kwargs)
            return self.user
    
class  Cart_item (models.Model):
     cart =models.ForeignKey(Cart, on_delete=models.CASCADE)
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     quantity = models.PositiveIntegerField(default =1)

     def __str__(self, *args, **kwargs):
          super().__str__(*args, **kwargs)
          return f" {self.product.name} x {self.quantity}"