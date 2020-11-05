from django.shortcuts import render
from django.http import  Http404
from todo.models import Task
from todo.serializers import TaskSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics

# Create your views here.
class TodoList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


