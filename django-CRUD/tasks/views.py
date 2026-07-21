from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,logout, authenticate
from django.db import IntegrityError
from .forms import CreateTask
from .models import task
from django.contrib.auth.decorators import login_required

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


def show_task(request):
    tasks = task.objects.filter(user = request.user, daycompleted__isnull=True)
    return render(request, 'task.html',{
        'tasks' : tasks
    })

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



