  
from django.shortcuts import render
from django.http import  Http404
from todo.models import Task
from todo.serializers import TaskSerializer,TasklikeSerializer
from todo.models import Task,Comments
from todo.serializers import TaskSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from todo.serializers import UserSerializer,CommentsSerializer
from rest_framework import permissions
from todo.permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from django.contrib.auth.models import User




class TodoList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CommentsList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class LikeListCreate(APIView):

    def get(self,request,pk):
        task = Task.objects.filter(pk=pk)
        # like_count = task.likepost.count()
        serializer = TaskSerializer(many=True)
        return Response(serializer.data)

    def task(self,request,pk):
        likeusers = request.user
        liketask = Task.objects.filter(pk=pk)
        serializer = TasklikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(likeusers,liketask)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

