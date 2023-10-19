from django.apps import AppConfig

#store applications specific configuration.

class FirstappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "firstApp"
