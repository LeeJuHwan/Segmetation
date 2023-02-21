from django.apps import AppConfig
from keras.models import load_model

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

