from django.urls import path
from . import views

urlpatterns = [
    path('', views.tradesman_home.as_view(), name='tradesman_home'),
]