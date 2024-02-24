from django.urls import path
from . import views

urlpatterns = [
    path('', views.tradesman_home, name='tradesman_home'),
]