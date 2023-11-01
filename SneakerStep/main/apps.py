from django.apps import AppConfig


# настройки конкретно приложения main,а не всего проекта
class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
