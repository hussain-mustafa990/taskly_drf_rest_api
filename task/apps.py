from django.apps import AppConfig


class TaskConfig(AppConfig):
    name = 'task'

    def ready(self):
        import task.signals
