from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.job_detail, name='job_detail'),
    path('', views.tradesman_home.as_view(), name='tradesman_home'),
    path('<slug:slug>/', views.user_detail, name='user_detail'),
]