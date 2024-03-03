from django.urls import path

from . import views

urlpatterns = [
    path('api/task-list/', views.task_list, name='task_list'),
    path('api/task-detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('api/task-create/', views.task_create, name='task_create'),
    path('api/task-update/<int:pk>/', views.task_update, name='task_update'),
    path('api/task-delete/<int:pk>/', views.task_delete, name='task_delete'),
]