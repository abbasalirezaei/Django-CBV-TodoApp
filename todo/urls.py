from django.urls import path

from .views import (
    TodoListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCompleteView,
    TaskUnCompleteView
)
app_name='todo'
urlpatterns = [
    path("", TodoListView.as_view(), name="index"),
    path("create/", TaskCreateView.as_view(), name="create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="update_task"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="delete_task"),
    path("complete/<int:pk>/", TaskCompleteView.as_view(), name="complete_task"),
    path("uncomplete/<int:pk>/", TaskUnCompleteView.as_view(), name="uncomplete_task"),

]
