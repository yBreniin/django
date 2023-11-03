from rest_framework import viewsets
from tasks.models import Task
from tasks.serializer import TaskSerializer

class TasksViewSet(viewsets.ModelViewSet):
    """Exibindo todos as tasks"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer