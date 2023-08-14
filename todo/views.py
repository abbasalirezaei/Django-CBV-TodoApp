from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task
from .forms import TaskForm


class TodoListView(ListView):
    model=Task
    context_object_name='tasks'
    template_name='todo/index.html'


class TaskCreateView(CreateView):
    model=Task
    form_class=TaskForm
    template_name='todo/create.html'
    success_url = reverse_lazy("todo:index")


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskCreateView, self).form_valid(form)

class TaskUpdateView(UpdateView):
    model = Task
    success_url = reverse_lazy("todo:index")
    form_class=TaskForm
    template_name = "todo/update.html"


class TaskDeleteView(LoginRequiredMixin, DeleteView):
	model = Task
	success_url = reverse_lazy("todo:index")
	template_name ="todo/task_confirm_delete.html"
