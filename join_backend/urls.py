"""
URL configuration for join_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from join.views import task_list, task_detail, login, register_user, contacts_list, contact_detail, category_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', task_list, name='task-list'),
    path('tasks/<int:pk>/', task_detail, name='task-detail'),
    path('contacts/', contacts_list, name='contacts_list'),
    path('contacts/<int:pk>/', contact_detail, name='contact_detail'),
    path('categories/', category_list, name='category-list'),
    
    # ------------------optional------------------ #
    path('register/', register_user, name='register'),
    path('login/', login, name='login'),
]
