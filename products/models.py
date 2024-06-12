from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
from django.urls import reverse
from django.db.models.query import Q
from django.conf import settings

from products.utils import slugify_product_name

# Create your models here.

User = settings.AUTH_USER_MODEL

class ProductQuerySet(models.QuerySet):
    
    def search_using_name_price(self,query=None):
        if query is None or query is  '':
            return self.none()
        lookups = Q(name__icontains=query) | Q(price__icontains=query)
        return self.filter(lookups)

class ProductManager(models.Manager):
    
    def get_queryset(self):
        return ProductQuerySet(model=self.model,query=self._db)
        
    def search(self,query):
        return self.get_queryset().search_using_name_price(query=query)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    slug = models.SlugField(max_length=50,blank=True,null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    
    products = ProductManager()
    
    def get_absolute_url(self):
        return reverse('product-details',kwargs={ 'product_slug' : self.slug })
    
@receiver(pre_save,sender=Product)    
def before_product_save(sender,instance,*args,**kwargs):
    if instance.slug is None:
        slugify_product_name(instance=instance)
        