from django.apps import AppConfig

class AuthenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.authen'

    def ready(self):
        import apps.authen.signals
