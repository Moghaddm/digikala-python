from django.http import HttpResponse
from django.shortcuts import render
from random import randint
from django.template.loader import render_to_string,get_template
from products.forms import ProductForm
from products.models import Product
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):
    random = randint(1,3)
    product = Product.objects.get(pk = random)
    
    context = {
        "my_list":[1,2,3,4,5,6],
        "object" : product,
        "objects" : Product.objects.all()
        }
    
    template = get_template("products/home-view.html")
    result = template.render(context=context)
    
    # HTTP_PARAGRAPH_TAGS= render_to_string("products/home-view.html",context=context)
    
    return HttpResponse(result)

def product_details(request,product_id,*args,**kwargs):
    product = get_object_or_404(Product,pk=product_id)
    
    temp = get_template("products/product-details.html")
    
    print(product.name)
    context = {
        "object" : product
    }
    
    return HttpResponse(temp.render(context=context))

def search_product(request):
    query = request.GET
    name = query.get('name')
    print(query is None)
    print(name is '')
    
    qs = Product.objects.all()
    if name is not '':
        qs = qs.filter(name__startswith=name)
        
    context= {
        "objects" : qs
    }
    
    return HttpResponse(render(request,"products/search.html",context=context))

@login_required
def create_product(request):
    form = ProductForm(request.POST or None)
    context = { "form" : form }
    if form.is_valid():
        product = form.save()
        context['object'] = product
        context['created'] = True
    return render(request,"products/create.html",context=context)
        
    