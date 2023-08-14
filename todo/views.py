from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm


class TodoListView(ListView):
    model=Task
    context_object_name='tasks'
    template_name='todo/index.html'


class CreateTask(CreateView):
    model=Task
    # fields = ["title",'details']
    form_class=TaskForm

    template_name='todo/create.html'
    success_url = reverse_lazy("todo:index")


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)
