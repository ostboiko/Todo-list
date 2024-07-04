from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from .forms import TaskForm, TagForm
from .models import Task, Tag


class HomeView(ListView):
    model = Task
    template_name = "catalog/home.html"
    context_object_name = "tasks"
    ordering = ["done", "-created_at"]


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "catalog/task_form.html"
    success_url = "/"


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "catalog/task_form.html"
    success_url = "/"


class TagListView(ListView):
    model = Tag
    template_name = "catalog/tag_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "catalog/tag_form.html"
    success_url = "/tags/"


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "catalog/tag_form.html"
    success_url = "/"


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "catalog/tag_confirm_delete.html"
    success_url = "/"


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "catalog/task_confirm_delete.html"
    success_url = "/"


class TaskToggleCompleteView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.done = not task.done
        task.save()
        return redirect("home")
