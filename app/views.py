from django.shortcuts import render

from .models import Task

from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, redirect

from .forms import TaskForm

from django.shortcuts import render, get_object_or_404, redirect

from django.shortcuts import get_object_or_404, redirect



def task_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'task_list.html', context)



def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {
        'task': task,
    }
    return render(request, 'task_detail.html', context)



def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            return redirect('task_detail', pk=new_task.pk)
    else:
        form = TaskForm()
    context = {
        'form': form,
    }
    return render(request, 'task_create.html', context)



def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    context = {
        'form': form,
        'task': task,
    }
    return render(request, 'task_update.html', context)



def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')