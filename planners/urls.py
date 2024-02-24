from django.urls import path
from . import views

urlpatterns = [
    path('', views.planner_home, name='planner_home'),
    path('user_list', views.UserList.as_view(), name='UserList'),
    path('<slug:slug>', views.user_detail, name="user_detail"),
]