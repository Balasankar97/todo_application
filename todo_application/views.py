from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from todo_application.models import Task


# Create your views here.
def home_page(request):
    try:
        tasks = Task.objects.filter(is_completed=False)
        completed_tasks = Task.objects.filter(is_completed=True)
        context = {
            'tasks': tasks, 
            'completed_tasks': completed_tasks
        }
    except Exception as err_msg:
        print('No Task objects')
    return render(request, 'todo_application/home.html', context=context)


def add_task(request):
    task = request.POST.get('task')
    print('task: ', task)
    Task.objects.create(task=task)
    return redirect('home_page')


def mark_as_done(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home_page')


def mark_as_undone(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home_page')


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    print('Task: ', task)
    if request.method == 'POST':
        updated_task = request.POST.get('task')
        task.task = updated_task
        task.save()
        return redirect('home_page')
    else:
        context = {'task': task}
        return render(request, 'todo_application/edit_task.html', context=context)
    
    
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home_page')