from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm, TagForm


class HomeView(View):
    template_name = "catalog/home.html"
    success_url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        task_form = TaskForm()
        tag_form = TagForm()
        context = {
            "tasks": tasks,
            "task_form": task_form,
            "tag_form": tag_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        task_form = TaskForm(request.POST)
        tag_form = TagForm(request.POST)
        if "submit_task" in request.POST and task_form.is_valid():
            task_form.save()
            return redirect(self.success_url)
        elif "submit_tag" in request.POST and tag_form.is_valid():
            tag_form.save()
            return redirect(self.success_url)
        tasks = Task.objects.all()
        context = {
            "tasks": tasks,
            "task_form": task_form,
            "tag_form": tag_form,
        }
        return render(request, self.template_name, context)
