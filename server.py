from flask import Flask, jsonify, request, render_template
import urllib, urllib2, json, string, time, base64, os, cv2
import numpy as np

app = Flask(__name__)

LABELED_DIRECTORY = 'static/labeled_images/'
CAPTCHA_DIRECTORY = 'static/captcha_images/'
images = os.listdir(CAPTCHA_DIRECTORY)
labeled_images = os.listdir(LABELED_DIRECTORY)

@app.route('/', methods = ['GET'])
def getPage():
    return render_template('label.html')

@app.route('/next', methods = ['GET'])
def getNextImage():
    #access your DB get your results here
    name = images[len(labeled_images)]
    data = {"name": CAPTCHA_DIRECTORY + name}
    return jsonify(data)

@app.route('/label', methods=['POST'])
def labelImage():
    name = request.form['name']
    label = request.form['label']
    labeled_images.append(name)
    output = LABELED_DIRECTORY + name[22:].split('.')[0] + '.txt'
    print output
    with open(output, 'w') as f:
        f.write(label)
    return 'success'