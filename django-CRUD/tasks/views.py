from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.db import IntegrityError
from .forms import CreateTask
from .models import task
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html',{
            'form' : UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #Resgistrar Usuario
           try:
                user = User.objects.create_user(username = request.POST['username'],
                                                password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('task')
           except IntegrityError: 
                return render(request,'signup.html',{
                'form' : UserCreationForm,
                'error': 'username already exist'
                })

            
        else:
            return render(request,'signup.html',{
            'form' : UserCreationForm,
            'error': 'Contraseña no coincide'
            })

@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html',{
            'form' : AuthenticationForm
        })
    else:
        user =  authenticate(request, username = request.POST['username'],
                                      password = request.POST['password'])
        if user is None:
            return render(request,'signin.html',{
            'form' : AuthenticationForm,
            'error':'Usuario no encontrado'})
        else:
             login(request,user)
             return redirect('task')


@login_required
def show_task(request):
    tasks = task.objects.filter(user = request.user, daycompleted__isnull=True)
    return render(request, 'task.html',{
        'tasks' : tasks
    })

@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request,'create_task.html',{
            'form': CreateTask 
        })
    else:
        try:
        #El usuario debe estar autenticado
            form = CreateTask(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('task')
        except ValueError:
             return render(request,'create_task.html',{
            'form': CreateTask 
        })

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        id_task = get_object_or_404(task, pk=task_id, user = request.user)
        form = CreateTask(instance = id_task)
        return render(request, 'task_detail.html',{
            'task':id_task,
            'form':form
        })
    else: 
        try:
            id_task = get_object_or_404(task, pk=task_id, user = request.user)
            form = CreateTask(request.POST, instance=id_task)
            form.save()
            return redirect('task')
        except ValueError:
           return render(request, 'task_detail.html',{
               'error':'Error'
           })


@login_required
def task_complete(request, task_id):
    completed = get_object_or_404(task, pk=task_id, user = request.user)
    if request.method =='POST':
        completed.daycompleted == timezone.now()
        completed.save()
        return redirect('task')

@login_required
def task_delete(request, task_id):
    delete_task = get_object_or_404(task, pk=task_id, user = request.user)
    if request.method == 'POST':
        delete_task.delete()
        return redirect('task') 

