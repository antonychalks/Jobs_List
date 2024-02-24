"""
URL configuration for job_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from planners import views as planner_views
from tradesman import views as tradesman_views
from main import views as main_views

urlpatterns = [
    path('', include("main.urls"), name='main-urls'),
    path('planners/', include("planners.urls"), name='planners-urls'),
    path('tradesman/', include("tradesman.urls"), name='tradesman-urls'),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
]
