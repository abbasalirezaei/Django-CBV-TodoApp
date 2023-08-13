from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task

class TodoListView(ListView):
    model=Task
    template_name='todo/index.html'