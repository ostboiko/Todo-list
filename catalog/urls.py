# catalog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/add/', views.add_task, name='add_task'),
    path('task/<int:pk>/update/', views.update_task, name='update_task'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('task/<int:pk>/complete/', views.complete_task, name='complete_task'),
    path('tags/', views.tag_list, name='tag_list'),
    path('tag/add/', views.add_tag, name='add_tag'),
    path('tag/<int:pk>/update/', views.update_tag, name='update_tag'),
    path('tag/<int:pk>/delete/', views.delete_tag, name='delete_tag'),
]
