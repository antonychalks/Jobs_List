from django.urls import path
from . import views

urlpatterns = [
    path('', views.planner_home, name='planner_home'),
    path('user_list', views.UserList.as_view(), name='UserList')
]