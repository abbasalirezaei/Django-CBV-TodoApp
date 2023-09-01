from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router=SimpleRouter()
router.register('task-list',views.TaskListViewSets,basename='task-list')
# router.register("task-list", ciewTaskListViewSets, basename="task_list")
# router.register(
#     "task-detail",
#     views.TaskDetailViewSets,
#     basename="task_detail",
# )
# router.register('category',views.CategoryModelViewSet,basename='category')

urlpatterns=router.urls
