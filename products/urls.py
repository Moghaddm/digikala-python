

from django.urls import path

from products import views


urlpatterns = [
    path('',view=views.home_view),
    path('search/',view=views.search_product,name='product-search'),
    path('create/',view=views.create_product,name='product-create'),
    path('<slug:product_slug>/',view=views.product_details,name='details'),
    path('update/<int:product_id>',view=views.update_product,name='product-update'),
    path('delete/<int:product_id>',view=views.delete_product,name='product-delete')
]