from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('complete/<int:task_id>/', views.completedTask, name='completedTask'),
    path('delete/<int:task_id>/', views.deleteTask, name='deleteTask'),
]
