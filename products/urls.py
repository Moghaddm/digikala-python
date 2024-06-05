

from django.urls import path

from products import views


urlpatterns = [
    path('',view=views.home_view),
    path('<int:product_id>/',view=views.product_details),
    path('search/',view=views.search_product),
    path('create/',view=views.create_product)
]