from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task


class TaskSerializers(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
class TasklikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasklike
        fields = '__all__'