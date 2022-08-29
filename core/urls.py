from django.urls import path
from .views import TaskList, TaskDeatil, TaskCreate

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),   
    path('task/<int:pk>/', TaskDeatil.as_view(), name='task'),   
    path('task-create/', TaskCreate.as_view(), name='task-create'),   
]