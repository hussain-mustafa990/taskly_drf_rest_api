from rest_framework import routers

from .viewsets import TaskListViewSet, TaskViewSet, AttachmentViewSet

app_name = 'task'

router = routers.DefaultRouter()
router.register('tasklists', TaskListViewSet)
router.register('tasks', TaskViewSet)
router.register('attachments', AttachmentViewSet)