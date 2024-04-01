from django.forms import ModelForm
from .models import Task
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput,TextInput
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']
       

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())


class TaskAddForm(forms.ModelForm):
    class Meta:
        model= Task
        fields='__all__'
   