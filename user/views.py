from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from .models import Todos

from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render




# Create your views here.
def home(request):
    if request.user.is_authenticated:
        t=Todos.objects.filter(user=request.user)
        return render(request,'user/index.html',{'t':t})
    else:
        return HttpResponseRedirect('/login/')


def LoginView(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            
            
            mail=request.POST.get('username')
            print(mail)
            passwd=request.POST.get('password')
            print(passwd)
            if mail!="" and passwd!="":
                user = authenticate(username=mail, password=passwd)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/')

                else:
                    return JsonResponse({"error":"authentication failed"})
        else:
            
            return render(request,'user/login.html',{})
        

                
            
    else:
        return HttpResponseRedirect('/')

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'user/register.html' 
    success_url = reverse_lazy('login')

def logout_user(request):
    
    logout(request)
    return HttpResponseRedirect('/login/')

def create_todo(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            txt=request.POST.get('todo')
            print(txt)
            t=Todos()
            t.user=request.user
            t.text=txt
            t.save()
            print('saved')
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')

def delete_todo(request,id):
    if request.user.is_authenticated:
        t=Todos.objects.get(id=id)
        t.delete()
        print('deleted')
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')

def save_edited(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            id=request.POST.get('todo_id')
            print(int(id))
            text=request.POST.get('todo')
            print(text)
            t=Todos.objects.get(id=id)
            t.text=text
            t.save()
            
            
            print('edited')
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')    
    
















