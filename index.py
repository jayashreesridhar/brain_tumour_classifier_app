#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 13:28:47 2020

@author: jayashree
"""
from __future__ import print_function 
from flask import render_template, request, redirect, flash

#import tensorflow as tf
from app import app
from werkzeug.utils import secure_filename
from main import getPrediction
import os
import time

import sys
#from werkzeug.serving import run_simple

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET','POST'])
#def index():
def submit_file():
    
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
            #return render_template('index.html')
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
            #return render_template('index.html')
        
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
            file_stats = os.stat(str(app.config['UPLOAD_PATH'])+'/'+filename)
            if file_stats.st_size > 5000000:
                flash('Please upload file with size less than 5MB')
                return redirect(request.url)
                #return render_template('index.html')
            tic = time.perf_counter()            
            label= getPrediction(filename)
            toc = time.perf_counter()
            print(f"Time taken for prediction {toc - tic:0.4f} seconds", file=sys.stderr)
            
            if(label):
                flash("The Scan Image "+filename+" has brain tumour")
            else:
                flash("The Scan Image "+filename+" doesn't have brain tumour")
            return redirect(request.url)
            #return render_template('index.html')
    return render_template('index.html')


if __name__ == "__main__":
    
    app.run('0.0.0.0')
    
    