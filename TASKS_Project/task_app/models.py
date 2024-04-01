from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

choice=[('Open','Open'),('In Progress','In Progress'),('Closed','Closed')]
        
class Task(models.Model):
    creater=models.CharField(max_length=60)
    task_name = models.CharField(max_length=80,null=True)
    content= models.CharField(max_length=400,null=True,blank=True)   
    status=models.CharField(max_length=20 ,choices=choice,default='open')
    user=models.ForeignKey(User,max_length=20,on_delete=models.CASCADE,null=True)
  

    def __str__(self):
        return self.creater

   

        
