#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 13:25:37 2020

@author: jayashree
"""

from flask import Flask
#from flask_debugtoolbar import DebugToolbarExtension
import pathlib

import tensorflow as tf
app = Flask(__name__)
# the toolbar is only enabled in debug mode:
#app.debug = True

#app.config['MAX_CONTENT_LENGTH'] = 5000 * 10
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['SECRET_KEY'] = '89765'
app.config['UPLOAD_PATH'] = pathlib.Path(__file__).parent / 'files_upload'
app.config['MODEL_PATH'] = pathlib.Path(__file__).parent / 'my_model/'
app.config['MODEL']=tf.keras.models.load_model(str(app.config['MODEL_PATH']))
#toolbar = DebugToolbarExtension(app)