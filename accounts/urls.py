
from django.urls import path

from accounts import views

urlpatterns=[
    path('login/',view=views.login_view),
    path('logout/',view=views.logout_view)
]