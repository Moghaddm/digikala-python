from django.contrib import admin

from products.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['price','name']
    search_fields= ['price','name']

admin.site.register(Product,ProductAdmin)