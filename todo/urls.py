from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todo import views

urlpatterns = [
     path('task/<int:pk>/like/',LikeListCreate.as_view(),name = 'task_likes'),
]
  

urlpatterns = format_suffix_patterns(urlpatterns)