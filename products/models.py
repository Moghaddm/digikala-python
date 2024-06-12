import random
from typing import Iterable
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
from django.urls import reverse

from products.utils import slugify_product_name

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    slug = models.SlugField(max_length=50,blank=True,null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    
    products = models.Manager()
    
    def get_absolute_url(self):
        return reverse('details',kwargs={ 'product_slug' : self.slug })
        # return f"products/{self.slug}"
    
@receiver(pre_save,sender=Product)    
def before_product_save(sender,instance,*args,**kwargs):
    if instance.slug is None:
        slugify_product_name(instance=instance)
    
    

    
    