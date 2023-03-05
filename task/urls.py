from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tasks, name='all_tasks'),
    path('completed/', views.completed_tasks_list, name='completed_tasks_list'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:task_id>', views.delete_task, name='delete_task'),
    path('complete/<int:task_id>', views.complete_task, name='complete_task'),
    path('detail/<int:task_id>', views.detail_task, name='detail_task'),
    path('update/<int:task_id>', views.update_task, name='update_task'),

    path('api/', views.TaskListView.as_view(), name='api_list'),
    path('api/create/', views.TaskCreateView.as_view(), name='api_create'),
    path('api/update/<int:pk>/', views.TaskDetailUpdateView.as_view(), name='api_detail_update'),
]
