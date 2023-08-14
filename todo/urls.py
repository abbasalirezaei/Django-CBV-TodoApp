from django.urls import path

from .views import TodoListView,TaskCreateView,TaskUpdateView
app_name='todo'
urlpatterns = [
    path("", TodoListView.as_view(), name="index"),
    path("create/", TaskCreateView.as_view(), name="create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="update_task"),
]
