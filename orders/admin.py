from django.contrib import admin


from django import forms
from orders.models import Order, OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    # readonly_fields = ['price']
    raw_id_fields = ['product']
    extra = 0
    
class OrderForm(admin.ModelAdmin):
    inlines = [OrderItemInline]
    class Meta:
        model = Order
        fields = '__all__'

admin.site.register(Order,OrderForm)