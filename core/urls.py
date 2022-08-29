from django.urls import path
from .views import TaskList, TaskDeatil, TaskCreate, TaskUpdate

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),   
    path('task/<int:pk>/', TaskDeatil.as_view(), name='task'),   
    path('task-create/', TaskCreate.as_view(), name='task-create'),   
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),   
]