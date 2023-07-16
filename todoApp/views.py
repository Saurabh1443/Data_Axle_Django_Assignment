from django.utils import timezone
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import todoList
from .forms import newTodo as createTodo ,Regestration ,Login,editTodo as changeTodo
from django.contrib.auth import authenticate ,login as loginuser,logout


# Get all Todo items created function----->
def home(request):
 
 if request.user.is_authenticated: 
       data =todoList.objects.filter(user = request.user)
       context = {"data":data}
       return render(request,template_name='index.html',context=context)
 else:
       return redirect('login') 
    

# Login function to create a Todo Item for yourself----->
def login(request):
    if request.method == "POST":
        form = Login(data=request.POST)
       
        if form.is_valid():  
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password = password)
            if user is not None:
              loginuser(request,user)
              return redirect('home')
        else:
          return render(request,template_name='login.html',context={'form':form})

    else :
        form = Login()
        return render(request,template_name='login.html',context={'form':form})
    
# New user signup function to create a Todo Item for yourself----->
def signup(request):
    if request.method == "POST":
        form = Regestration(request.POST)
        if form.is_valid():  
            user = form.save()
            return redirect('home')
        else:
          return render(request,template_name='signup.html',context={'form':form})

    else :
        form = Regestration()
        return render(request,template_name='signup.html',context={'form':form})

# Function to create a Todo Item for yourself----->
def newTodo(request):
  
  if request.user.is_authenticated:  
   if request.method == "POST":
        form = createTodo(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
        else:
          return render(request,template_name="post.html", context={"form":form})
    
   else :
        form = createTodo()
        return render(request,template_name='post.html',context={'form':form})
  else:
       return redirect('login')
  
  
#Function to edit a Todo item ----->
def editTodo(request,id):
   
 if request.user.is_authenticated: 
    if request.method == "POST":
     data =todoList.objects.get(pk=id)
     form= changeTodo(request.POST, instance=data)
     if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
     else:
          return render(request,template_name="edit.html", context={"form":form})
 
    else :
        data =todoList.objects.get(pk=id)
        form = changeTodo(instance=data)
        return render(request,template_name='edit.html',context={'form':form})
 else:
     return redirect('login') 
 

#Function to delete a Todo item ----->
def deleteTodo(request,id):
  if request.user.is_authenticated:   
     todoList.objects.get(pk=id).delete()
     return redirect('home')
  else:
     return redirect('login')  
  

#Function to edit the status of a Todo item ----->    
def editTodoStatus (request,id,status):
  if request.user.is_authenticated:  
    data =todoList.objects.get(pk=id)
    data.is_completed= True if status==1 else False
    data.save()
    return redirect('home')
  else:
     return redirect('login')  

# Logout user function ----->

def Logout(request):
   logout(request)
   return redirect('login')


#Welcome function when user first visits the app----->

def welcome(request):
   if request.user.is_authenticated==False:
     return redirect('login')
   else:
      return redirect('home')