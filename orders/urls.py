


from django.urls import path
from orders import views

urlpatterns = [
    path('',view=views.orders_list)
]