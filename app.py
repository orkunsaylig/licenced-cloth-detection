from fileinput import filename
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from werkzeug.utils import secure_filename

import os
import gc
import sys
import json
import glob
import random
from pathlib import Path
 

import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
import itertools
from tqdm import tqdm



UPLOAD_FOLDER = 'static/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'OrkunSaylig'  


app.config['UPLOADED_PHOTOS_DEST'] =  os.getcwd() + '/static'

@app.route('/', methods=['GET'])
def home_page():
    return render_template('home.html')


@app.route("/upload", methods=['GET', 'POST'])
def succes():
    if request.method == 'POST':  
        f = request.files['file']  
        if f.filename == '':
            return render_template("home.html")

        f.save(UPLOAD_FOLDER + f.filename)  
        
        full_filename = os.path.join("static", f.filename)

        th = cv2.imread(UPLOAD_FOLDER + f.filename, 0)
        th = cv2.Canny(th,100,200)
        th_path = os.path.join("static/output", f.filename)

        cv2.imwrite(th_path, th)

        
        files = list()
        files.append(f.filename)
        files.append("output/" + f.filename)



        
        return render_template("upload.html", user_file = files)  









if __name__ == '__main__':
    app.run(port=3000, debug=True)