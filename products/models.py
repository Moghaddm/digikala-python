import random
from typing import Iterable
from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import pre_save,post_save

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    slug = models.SlugField(max_length=50,blank=True,null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    
    prodcuts = models.Manager()
    
def slugify_product_name(instance,save=False,new_slug=None):
    if new_slug is None:
        slug = slugify(instance.name)
    else:
        slug = new_slug
    qs = Product.prodcuts.filter(slug =slug ).exclude(pk = instance.id)
    if qs.exists():
        rand = random.randint(300_000,500_000)
        slug = f"{slug}-{rand}"
        return slugify_product_name(instance,save=True,new_slug = slug)
    instance.slug= slug
    if save:
        instance.save()
    return instance

@receiver(pre_save,sender=Product)    
def before_product_save(sender,instance,*args,**kwargs):
    if instance.slug is None:
        slugify_product_name(instance=instance)
    
    

    
    