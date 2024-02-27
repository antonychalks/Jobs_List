from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.landing_page, name='home'),
]
