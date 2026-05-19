from django.urls import path
from task_mgmt.views import TaskView, update_task, delete_task

urlpatterns = [
    path('task/', TaskView, name="Task-page"), 
    path('update-task/',update_task),
    path('delete-task/', delete_task),
]
