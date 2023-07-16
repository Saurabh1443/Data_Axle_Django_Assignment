from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class todoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=150)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    is_completed=models.BooleanField(default=False)


    
    
    