from todo.models import Task
from rest_framework import viewsets
from todo.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
