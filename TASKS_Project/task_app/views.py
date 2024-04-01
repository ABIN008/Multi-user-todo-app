from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import RegForm,LoginForm, TaskAddForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import DeleteView
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return render(request, "index.html")


def signup(request):
    form=RegForm()
    if request.method=='POST':
        form=RegForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You are registered Successfully !!!")
            return redirect('login')
    context={'form':form}
    return render(request,"signup.html",context=context)


def login(request):
    form=LoginForm
    if request.method=='POST':
        form= LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)
                messages.success(request, "You are logged in Successfully !!!")
                return redirect('userindex')
            
    context={'form':form}
    return render(request,"login.html",context=context)

@login_required(login_url='login')
def userindex(request):
    return render(request,"userindex.html")

@login_required(login_url='login')
def TaskAdd(request):
    form=TaskAddForm(request.POST)
    task=Task.objects.all()
    
    if request.method =='POST':
        form=TaskAddForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            form.save()
            messages.success(request, "New task created Successfully !!!")
            return redirect('taskview')

    context={'form':form}
    return render(request, 'addtask.html',context=context)



@login_required(login_url='login')
def TaskView(request): 
    current_user = request.user.id
    task=Task.objects.all().filter(user=current_user)   
    context={'task':task}
    return render(request, 'taskview.html',context=context)


@login_required(login_url='login')
def TaskAssign(request):  
    task=Task.objects.filter(creater=request.user)
    context={'task':task}
    return render(request,'assigntask.html',context=context)

# @login_required(login_url='login')
# def TaskAssign(request):  
#     task=Task.objects.filter(creater=request.user)
#     context={'task':task}
#     return render(request,'assigntask.html',context=context)

@login_required(login_url='login')
def EditTask(request,pk):
    task=Task.objects.get(id=pk)
    form= TaskAddForm(request.POST or None,instance=task)
    if request.method=='POST':
        form= TaskAddForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated Successfully !!!")
            return redirect('taskview')
    context={'form':form}
    return render(request, 'edittask.html',context=context)


@login_required(login_url='login')
def TaskDelete(request,pk):
    task=Task.objects.get(id=pk)   
    if request.method=='POST':
        task.delete()
        messages.success(request, "Task Deleted Successfully !!!")
        return redirect('assign')
    
    context={'object':task}
    return render(request, 'taskdelete.html',context=context)


def logout(request):
    auth.logout(request)
    messages.success(request, "You are logged out Successfully !!!")
    return redirect("home")
