from django.apps import AppConfig
from keras.models import load_model
from PIL import Image
import numpy as np
import time
import os, sys
import cv2
import pandas as pd

from model import pill_model

os.environ["CUDA_VISIBLE_DEVICES"]="-1"

cur_dir = os.path.dirname(__file__)
# print(cur_dir)
efn_path = "/home/lab06/Segmetation/pill/module/efn_models"
class LoadConfig(AppConfig):
  start = time.time()
  pill_module = pill_model()

  
  ### compile memory 
  # memory_loading = Image.open("/home/lab06/drug.png")
  memory_loading = "/home/lab06/Segmetation/backend/static/img/test_predict.jpg"
  # memory_loading = memory_loading.convert("L")
  # memory_loading = memory_loading.resize((224,224))
  # memory_loading = np.asarray(memory_loading)
  # memory_loading = memory_loading.reshape(1, memory_loading.shape[0], memory_loading.shape[1], 1)
  pill_module.predict_shorten(memory_loading)
  print("logging tracking and memory optimization")
  print("logging  sec :", time.time() - start)


  def ready(self):
    pass