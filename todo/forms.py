from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter the title of your task...'}
                ),
        label='Title'
            
    )
    
    details = forms.CharField(
        # help_text='Required: First Name',
        widget=forms.TextInput(attrs={'placeholder': 'add some details'}
                ),
        label='Detail'
            
    )
    class Meta:
        model = Task
        fields = ['author','title', 'details']
