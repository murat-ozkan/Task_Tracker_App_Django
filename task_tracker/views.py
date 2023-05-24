from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import TaskTracker, TaskTrackerSerializer

class TaskTrackerView(ModelViewSet):
    queryset = TaskTracker.objects.all()
    serializer_class = TaskTrackerSerializer

