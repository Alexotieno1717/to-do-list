from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task,Comments
from .models import Task



class TasklikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasklike
        fields = '__all__'



class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ['id', 'owner', 'title', 'description', 'time']
        

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']

class CommentsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comments
        fields = ['comment','user','task']

