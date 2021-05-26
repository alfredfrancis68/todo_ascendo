from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets,permissions
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.routers import DefaultRouter

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]


todo_list = TodoViewSet.as_view({
    'get':'list',
    'post':'create',
})

todo_detail = TodoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

# Use routers for binding viewsets to urls