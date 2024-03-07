from django.urls import path
from . import views

urlpatterns = [
    path('', views.tradesman_home.as_view(), name='tradesman_home'),
    path('<slug:slug>/', views.job_detail, name='job_detail'),
    path('<slug:slug>/', views.user_detail, name='user_detail'),
    path('<slug:slug>/edit_task/<int:task_id>/',
         views.task_edit, name='task_edit'),
    path('<slug:slug>/delete_task/<int:task_id>/',
         views.task_delete, name='task_delete'),
]