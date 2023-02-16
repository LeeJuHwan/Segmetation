import numpy as np
from PIL import Image
import pickle
from keras.models import load_model
import asyncio
import time
# from django.core.cache import cache
from api.load import LoadConfig

start = time.time()
with open("api/index.pkl", "rb") as r :
    index = pickle.load(r)


# def cnn():
#     cache_key = load_model("api/best_cvision", compile=False)
#     model = cache.get_or_set(cache_key, "my_model")
#     return model

# model = cnn()
# model = LoadConfig.model
# model = load_model("api/best_cvision", compile=False)
# memory_loading = Image.open("/home/lab06/drug.png")
# memory_loading = memory_loading.convert("L")
# memory_loading = memory_loading.resize((224,224))
# memory_loading = np.asarray(memory_loading)
# memory_loading = memory_loading.reshape(1, memory_loading.shape[0], memory_loading.shape[1], 1)
# print("logging tracking and memory optimization")
# print("logging  sec :", time.time() - start)

async def shape_pred(path_:str, model_) -> str:
    start = time.time()
    """_summary_

    Args:
        path_ (str): _description_

    Returns:
        str: _description_
    """
    loop = asyncio.get_running_loop()
    x = await loop.run_in_executor(None, Image.open, path_)
    # print("loop config sec :", time.time() - start)

    x = Image.open(path_)
    # print("img open sec :", time.time() - start)
    x = x.resize((224,224))
    x = x.convert("L")
    x = np.asarray(x)
    x = x.reshape(1, x.shape[0], x.shape[1], 1)
    # print("reshape sec :", time.time() - start)
    output = await loop.run_in_executor(None, model_.predict, x)
    print("result sec :", time.time() - start)
    return index[np.argmax(output)]