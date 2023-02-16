import os
import re

import cv2
import torch
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
from rembg import remove
    
def cv2plt(opencv_img):
    return cv2.cvtColor(opencv_img, cv2.COLOR_BGR2RGB)

def cv2pil(opencv_img):
    return Image.fromarray(cv2.cvtColor(opencv_img, cv2.COLOR_BGR2RGB))
    
def pil2cv(pil_img):
    return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)


class pill_preprocess:
    
    def __init__(self):
        pass
    
    def weaken_light(self, opencv_img):
        hsv_img = cv2.cvtColor(opencv_img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_img)

        b_3 = np.where(v<255*0.3, 1, 0)
        b_5 = np.where(v<255*0.5, np.where(v>255*0.3, 1, 0), 0)
        b_9 = np.where(v>255*0.9, 1, 0)
        _b_3 = 1-b_3
        av_bright = np.sum(cv2.multiply(1.0*_b_3,1.0*v)) / np.sum(_b_3)

        b_w = cv2.add(cv2.add(1.0* b_3,0.7 * b_5), -0.5*b_9)
        v = v.astype(float)
        b_w = b_w.astype(float)
        g_v = cv2.GaussianBlur(v, (0, 0), 1).astype(float)
        g_w = cv2.GaussianBlur(b_w, (0, 0), 10).astype(float)

        revision_v = cv2.add(v, cv2.multiply(cv2.subtract(av_bright,g_v),g_w))
        revision_v = np.where(revision_v<0, 0, revision_v)
        revision_v = np.where(revision_v>255, 255, revision_v)
        revision_v = revision_v.astype(h.dtype)

        result = cv2.cvtColor(cv2.merge([h, s, revision_v]), cv2.COLOR_HSV2BGR)

        return result
    
    def remove_background(self, opencv_img):
        pil_image = cv2pil(opencv_img)
        output_1 = remove(pil_image)

        result = cv2.cvtColor(np.array(output_1), cv2.COLOR_RGB2BGR)
        return result
    
    def image_sort(self, opencv_img):
        pil_img = cv2pil(opencv_img)
        cropped = pil_img.crop(pil_img.getbbox())
        result = pil2cv(cropped)
        return result
    
    def resize_img(self, opencv_img):
        size = (224, 224)
        base_pic = np.zeros((size[0],size[1],3),np.uint8)
        pic1 = opencv_img
        h,w = pic1.shape[:2]
        
        ash = size[1]/h
        asw = size[0]/w
        
        if asw < ash:
            sizeas=(int(w*asw),int(h*asw))
        else:
            sizeas=(int(w*ash),int(h*ash))
        
        pic1 = cv2.resize(pic1,dsize=sizeas, interpolation=cv2.INTER_LINEAR)
        base_pic[int(size[1]/2-sizeas[1]/2):int(size[1]/2+sizeas[1]/2),
        int(size[0]/2-sizeas[0]/2):int(size[0]/2+sizeas[0]/2),:] = pic1

        result = base_pic
        
        return result
    
    def replace_blacklike(self, opencv_img):
        black_like_mask = cv2.bitwise_not(cv2.inRange(opencv_img, (0, 0, 0), (10, 10, 10)))
        result = cv2.bitwise_and(opencv_img, opencv_img, mask=black_like_mask) 
        
        return result
    
    def preprocess(self, opencv_img):
        result = self.weaken_light(opencv_img)
        result = self.remove_background(result)
        result = self.image_sort(result)
        result = self.resize_img(result)
        
        return result