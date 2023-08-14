from django.urls import path

from .views import TodoListView,CreateTask
app_name='todo'
urlpatterns = [
    path("", TodoListView.as_view(), name="index"),
    path("create/", CreateTask.as_view(), name="create")
]
