  
from django.shortcuts import render
from django.http import  Http404
from todo.models import Task
from todo.serializers import TaskSerializer,TasklikeSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from todo.serializers import UserSerializer
from rest_framework import permissions
from todo.permissions import IsOwnerOrReadOnly

class LikeListCreate(APIView):

    def get(self,request,pk):
        task = Task.objects.filter(pk=pk)
        like_count = task.likepost.count()
        serializer = TaskSerializer(like_count,many=True)
        return Response(serializer.data)

    def task(self,request,pk):
        likeusers = request.user
        liketask = Task.objects.filter(pk=pk)
        serializer = TasklikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(likeusers,liketask)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
