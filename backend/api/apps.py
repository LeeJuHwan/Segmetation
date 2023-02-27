from django.apps import AppConfig
from keras.models import load_model
import os

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self) :
        # if not os.environ.get("APP") :
        #     os.environ["APP"] = True
        #     print("한번만 실행")
        pass
        
