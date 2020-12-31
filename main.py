#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 20:06:21 2020

@author: jayashree
"""
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1" 
import tensorflow as tf #open source library for numerical computation that makes machine learning faster and easier.

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from app import app
model=tf.keras.models.load_model(str(app.config['MODEL_PATH']))


def getPrediction(filename):

    
    
    image = load_img(str(app.config['UPLOAD_PATH'])+'/'+filename, target_size=(350, 350))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    
    pred_prob = model.predict(image)
    pred_bool = (pred_prob >= 0.5).item()
   
    
    return pred_bool