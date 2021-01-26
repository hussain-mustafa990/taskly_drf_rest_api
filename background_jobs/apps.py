from django.apps import AppConfig


class BackgroundJobsConfig(AppConfig):
    name = 'background_jobs'

    def ready(self):
        import background_jobs.tasks
