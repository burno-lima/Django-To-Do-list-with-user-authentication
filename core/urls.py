from django.urls import path
from .views import TaskList, TaskDeatil

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),   
    path('task/<int:pk>/', TaskDeatil.as_view(), name='task'),   
]