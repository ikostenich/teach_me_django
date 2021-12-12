from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users_app'

    def ready(self) -> None:
        from .signals import create_user_profile
        super().ready()