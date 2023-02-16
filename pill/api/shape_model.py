from keras.models import load_model
from django.apps import AppConfig

class LoadConfig(AppConfig):
    model = load_model('/home/lab06/docker_server/pill/api/best_cvision', compile = False)

    def ready(self):
        pass