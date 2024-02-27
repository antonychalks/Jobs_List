from django.urls import path
from . import views
from django.urls import path, include
from planners import views as planner_views
from tradesman import views as tradesman_views
from main import views as main_views

urlpatterns = [
    path('', views.landing_page, name='home'),
]
