from django.apps import AppConfig


class OrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # or 'django.db.models.AutoField'
    
    name = 'order'
