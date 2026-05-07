from django.apps import AppConfig


class AppMovieConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_movie'

    def ready(self):
        import app_movie.signals  # noqa: F401
