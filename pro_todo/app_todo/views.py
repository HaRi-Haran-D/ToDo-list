from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def home(request):
    tasks = Todo.objects.all().order_by('created_at')
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title)
        return redirect('home')
    return render(request, 'app_todo/base.html', {'tasks':tasks})

def completedTask(request,task_id):
    task = Todo.objects.get(id = task_id)
    task.completed=True
    task.save()
    return redirect(home)

def deleteTask(request, task_id):
    task = Todo.objects.get(id = task_id)
    task.delete()
    return redirect(home)