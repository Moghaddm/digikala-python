from django.http import HttpResponse
from django.shortcuts import redirect, render
from random import randint
from django.template.loader import render_to_string,get_template
from products.forms import ProductForm
from products.models import Product
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):
    random = randint(1,3)
    product = Product.prodcuts.get(pk = random)
    context = {
        "my_list":[1,2,3,4,5,6],
        "object" : product,
        "objects" : Product.prodcuts.all()
        }
    template = get_template("products/home-view.html")
    result = template.render(context=context)
    return HttpResponse(result)

@login_required
def product_details(request,product_id,*args,**kwargs):
    product = get_object_or_404(Product,pk=product_id)
    temp = get_template("products/product-details.html")
    context = {
        "object" : product
    }
    print('----')
    return HttpResponse(temp.render(context=context))

def search_product(request):
    query = request.GET
    name = query.get('name')
    qs = Product.prodcuts.all()
    if name is not '':
        qs = qs.filter(name__startswith=name)
    context= {"objects" : qs}
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

@login_required
def update_product(request,product_id):
    product = Product.prodcuts.get(pk=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(f'/products/{product.id}')
    context = {'form' : form,'product' : product}
    return render(request,'products/update.html',context=context)

@login_required
def delete_product(request,product_id):
    # if request.method == 'POST':
    product = Product.prodcuts.get(pk = product_id)
    product.delete()
    return redirect('/products')  
    # return HttpResponse("<h1>cannot delete</h1>")    
    

        
    