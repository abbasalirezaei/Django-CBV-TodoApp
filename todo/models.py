from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Task(models.Model):
    """
    This is a simple task models for our todo app   
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(max_length=200)
    details = models.TextField(blank=True, null=True,max_length=300)
    isCompleted = models.BooleanField(default=False)
    
    created_date =  models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_date',)

    def get_short_content(self):
        return self.details[:5]