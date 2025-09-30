from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # if user is deleted, delete their tasks too
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) 
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True) # sets the field to now when the object is first created

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']  # incomplete tasks appear first
