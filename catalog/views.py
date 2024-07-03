from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Tag
from .forms import TaskForm, TagForm


def home(request):
    tasks = Task.objects.all().order_by("done", "-created_at")
    return render(request, "catalog/home.html", {"tasks": tasks})


def task_form_view(request, pk=None):
    if pk:
        task = get_object_or_404(Task, pk=pk)
    else:
        task = None

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task)

    return render(request, "catalog/task_form.html", {"form": form})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "catalog/tag_list.html", {"tags": tags})


def update_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TagForm(instance=tag)
    return render(request, "catalog/tag_form.html", {"form": form})


def delete_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('home')
    return render(request, "catalog/tag_confirm_delete.html", {"tag": tag})


def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tag_list')
    else:
        form = TagForm()
    return render(request, "catalog/tag_form.html", {"form": form})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm()
    return render(request, "catalog/task_form.html", {"form": form})


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task)
    return render(request, "catalog/task_form.html", {"form": form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('home')
    return render(request, "catalog/task_confirm_delete.html", {"task": task})


def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()
    return redirect("home")
