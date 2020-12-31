#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 13:28:47 2020

@author: jayashree
"""

from flask import render_template, request, redirect, flash


from app import app
from werkzeug.utils import secure_filename
from main import getPrediction
import os
#import time
from werkzeug.serving import run_simple

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET','POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
            file_stats = os.stat(str(app.config['UPLOAD_PATH'])+'/'+filename)
            if file_stats.st_size > 5000000:
                flash('Please upload file with size less than 5MB')
                return redirect(request.url)
            #tic = time.perf_counter()
            label= getPrediction(filename)
            #toc = time.perf_counter()
            #print(f"Time taken for prediction {toc - tic:0.4f} seconds")
            
            if(label):
                flash("The Scan Image "+filename+" has brain tumour")
            else:
                flash("The Scan Image "+filename+" doesn't have brain tumour")
            return redirect('/')


if __name__ == "__main__":
    run_simple('0.0.0.0', 5000, app, use_reloader=True)
    
    