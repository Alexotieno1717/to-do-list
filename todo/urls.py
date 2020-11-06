from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todo import views

urlpatterns = [

    path('task/<int:pk>/like/',LikeListCreate.as_view(),name = 'task_likes'),
    path('todo/', views.TodoList.as_view()),
    path('todo/<int:pk>/', views.TodoDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('comments/'views.CommentsList.as_view()),
    path('comments/<int:pk>/', views.CommentsDetail.as_view()),

]


urlpatterns = format_suffix_patterns(urlpatterns)