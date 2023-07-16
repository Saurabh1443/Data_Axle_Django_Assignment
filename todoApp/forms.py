from django import forms
from .models import todoList
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm

class newTodo(forms.ModelForm):
    class Meta:
        model = todoList
        fields=('title','description','start_date','end_date','is_completed',)
        
class editTodo(forms.ModelForm):
    class Meta:
        model = todoList
        fields=('title','description','start_date','end_date',)        

class Regestration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']    

class Login(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')              