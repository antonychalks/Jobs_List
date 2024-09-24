from django.urls import path
from . import views

urlpatterns = [
    path('add_user', views.add_user, name="add_user"),
    path('<slug:slug>/', views.user_detail, name='user_detail'),
    path('user_list', views.UserList.as_view(), name='UserList'),
    path('<slug:slug>/edit_job/<int:job_id>/',
         views.job_edit, name='job_edit'),
    path('delete_job/<int:job_id>/',
         views.job_delete, name='job_delete'),
    path('', views.planner_home, name='planner_home'),
]
