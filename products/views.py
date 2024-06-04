from django.http import HttpResponse
from django.shortcuts import render
from random import randint
from django.template.loader import render_to_string,get_template
from products.models import Product

# Create your views here.

def home_view(request):
    random = randint(1,3)
    product = Product.objects.get(pk = random)
    
    context = {"object" : product}
    
    template = get_template("products/home-view.html")
    result = template.render(context=context)
    
    
    # HTTP_PARAGRAPH_TAGS= render_to_string("products/home-view.html",context=context)
    
    return HttpResponse(result)