from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router=SimpleRouter()
router.register('task-list',views.TaskListViewSets,basename='task-list')
urlpatterns=router.urls
