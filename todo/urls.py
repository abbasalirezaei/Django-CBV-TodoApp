from django.urls import path

from .views import TodoListView
app_name='todo'
urlpatterns = [
    path("", TodoListView.as_view(), name="index")
]
