# urls.py
from django.urls import path
from .views import (
    HomeView, TaskCreateView, TaskUpdateView, TagListView,
    TagCreateView, TagUpdateView, TagDeleteView, TaskDeleteView, TaskToggleCompleteView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('task/new/', TaskCreateView.as_view(), name='add_task'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
    path('task/<int:pk>/complete/', TaskToggleCompleteView.as_view(), name='complete_task'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tag/new/', TagCreateView.as_view(), name='add_tag'),
    path('tag/<int:pk>/edit/', TagUpdateView.as_view(), name='update_tag'),
    path('tag/<int:pk>/delete/', TagDeleteView.as_view(), name='delete_tag'),
]
