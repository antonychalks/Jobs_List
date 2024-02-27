from django.urls import path
from . import views

urlpatterns = [
    path('add_user', views.add_user, name="add_user"),
    path('<slug:slug>/', views.user_detail, name='user_detail'),
    path('user_list', views.UserList.as_view(), name='UserList'),
    path('', views.planner_home, name='planner_home'),
]