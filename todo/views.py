from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView,View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task
from .forms import TaskForm
from .filters import TaskFilter

class TodoListView(LoginRequiredMixin,ListView):
    model=Task
    context_object_name='tasks'
    template_name='todo/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TaskFilter(self.request.GET, queryset=self.get_queryset())
        return context
        
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)
        

class TaskCreateView(LoginRequiredMixin,CreateView):
    model=Task
    form_class=TaskForm
    template_name='todo/create.html'
    success_url = reverse_lazy("todo:index")


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskCreateView, self).form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    success_url = reverse_lazy("todo:index")
    form_class=TaskForm
    template_name = "todo/update.html"


class TaskDeleteView(LoginRequiredMixin, DeleteView):
	model = Task
	success_url = reverse_lazy("todo:index")
	template_name ="todo/task_confirm_delete.html"

class TaskCompleteView(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("todo:index")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.isCompleted = True
        object.save()
        return redirect(self.success_url)

class TaskUnCompleteView(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("todo:index")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.isCompleted = False
        object.save()
        return redirect(self.success_url)
