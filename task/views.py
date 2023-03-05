from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from .serializers import TaskSerializer, TaskDetailSerializer, TaskCreateSerializer, TaskUpdateSerializer
from rest_framework import generics


def all_tasks(request):
    tasks = Task.objects.filter(completed=False)
    return render(request, 'index.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task = Task(title=title, description=description)
        task.save()
    return redirect('all_tasks')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('all_tasks')


def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.completed_at = datetime.now()
    task.save()
    return redirect('all_tasks')


def completed_tasks_list(request):
    tasks = Task.objects.filter(completed=True)
    return render(request, 'completed_tasks.html', {'tasks': tasks})


def detail_task(request, task_id):
    task_detail = Task.objects.get(id=task_id)
    return render(request, 'detail_task.html', {'task_detail': task_detail})


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        form.save()
        return redirect('all_tasks')
    else:
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task,
    }
    return render(request, 'index.html', context=context)


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


class TaskDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    update_serializer_class = TaskUpdateSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return self.update_serializer_class
        return self.serializer_class
