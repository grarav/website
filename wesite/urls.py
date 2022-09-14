from django.urls import path
from .views import TaskList
from .views import home

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),


]
