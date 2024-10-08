from django.urls import path
from . import views
from planners import views as planner_views

urlpatterns = [
    path('', views.Tradesman_Home.as_view(), name='tradesman_home'),
    path('<slug:slug>/', views.job_detail, name='job_detail'),
    path('<slug:slug>/', planner_views.user_detail, name='user_detail'),
    path('<slug:slug>/edit_task/<int:task_id>/',
         views.task_edit, name='task_edit'),
    path('<slug:slug>/delete_task/<int:task_id>/',
         views.task_delete, name='task_delete'),
    path('<slug:slug>/assign_tradesmen/<int:task_id>/',
         views.assign_tradesmen, name='assign_tradesmen'),
]
