from django.apps import AppConfig
from keras.models import load_model
from PIL import Image
import numpy as np
import time

class LoadConfig(AppConfig):
   start = time.time()
   model = load_model("api/best_cvision", compile=False)
    ### compile memory 
   memory_loading = Image.open("/home/lab06/drug.png")
   memory_loading = memory_loading.convert("L")
   memory_loading = memory_loading.resize((224,224))
   memory_loading = np.asarray(memory_loading)
   memory_loading = memory_loading.reshape(1, memory_loading.shape[0], memory_loading.shape[1], 1)
   model.predict(memory_loading)
   print("logging tracking and memory optimization")
   print("logging  sec :", time.time() - start)

   def ready(self):
     pass