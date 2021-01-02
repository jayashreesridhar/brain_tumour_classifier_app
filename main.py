#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 20:06:21 2020

@author: jayashree
"""
from __future__ import print_function 
#import tensorflow as tf #open source library for numerical computation that makes machine learning faster and easier.

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from app import app
import sys






# Set CPU as available physical device
#my_devices = tf.config.experimental.list_physical_devices(device_type='CPU')
#tf.config.experimental.set_visible_devices(devices= my_devices, device_type='CPU')

# To find out which devices your operations and tensors are assigned to
#tf.debugging.set_log_device_placement(True)
def getPrediction(filename,model):
    #global model
    #model=tf.keras.models.load_model(str(app.config['MODEL_PATH']))
    print("inside prediction before model loading", file=sys.stderr)
    image = load_img(str(app.config['UPLOAD_PATH'])+'/'+filename, target_size=(350, 350))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    print("after model loading and before predict", file=sys.stderr)
    pred_prob = model.predict(image)
    print("after predict", file=sys.stderr)
    pred_bool = (pred_prob >= 0.5).item()
   
    
    return pred_bool