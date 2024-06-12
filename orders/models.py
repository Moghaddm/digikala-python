from django.conf import settings
from django.db import models
from products.models import Product

# Create your models here.

class Order(models.Model):  
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,on_delete=models.SET_NULL)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    payment_method = models.CharField(max_length=40)
    total_price = models.IntegerField(max_length=1_000_000_000)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=40)
    price = models.IntegerField(max_length=400_000_000,null=False)
    
    
    

    
    