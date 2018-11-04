import json
import logging
import os
import pickle
import webapp2
from flask import Flask, request, send_file
from PIL import Image

# import torch
# import torchvision.transforms as transforms
# import torchvision

import cloudstorage as gcs
from google.cloud import storage
from google.appengine.api import app_identity
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers


app = Flask(__name__)

@app.before_first_request
def init():
    # Need to set this for local dev - see https://groups.google.com/forum/#!topic/google-appengine/LiwVqZvlO8A
    gcs.common.set_access_token("ya29.GltJBrS6fFMoCG5tEq1nO7TvD9v8z4mJ8WtC_tpTpa0rSSeegJdHHyeoUtc368ko7s9vAfz_edmFdo0cDwB4QOh_VUJdnYziyhljnKUVB4Ti-DjsS-sr6lovPytA")

@app.route('/', methods=['GET'])
def index():    
    # Setup bucket
    storage_client = storage.Client()
    bucket_name = os.environ['MODEL_BUCKET']
    bucket = storage_client.get_bucket(bucket_name)

    # Load image from bucket and create PIL
    raw_image = gcs.open('/color-wave-bucket/paintschainer.jpg')
    A_img = Image.open(raw_image).convert('RGB')
    ratio = A_img.width / A_img.height

    # Do some transforms
    # transform_list = [transforms.Resize((256,256)), transforms.ToTensor(),
    #                    transforms.Normalize((0.5, 0.5, 0.5),
    #                                         (0.5, 0.5, 0.5))]
    # allTransforms = transforms.Compose(transform_list)
    
    return "works", 200

@app.route('/image', methods=['GET'])
def image():
    image_url = "https://storage.cloud.google.com/color-wave-bucket/paintschainer.jpg"
    return image_url, 200

@app.route('/return_image', methods=['GET'])
def returnImage():
    print ("WORKING")
    storage_client = storage.Client()
    bucket_name = os.environ['MODEL_BUCKET']
    bucket = storage_client.get_bucket(bucket_name)
    image = gcs.open('/color-wave-bucket/paintschainer.jpg')

    print(image)

    return send_file(image, mimetype='image/gif')

# Lists the contents of the bucket
@app.route('/bucket', methods=['GET'])
def bucket():
    storage_client = storage.Client()
    bucket_name = os.environ['MODEL_BUCKET']
    bucket = storage_client.get_bucket(bucket_name)

    blobs = bucket.list_blobs()

    contents = ""
    for blob in blobs:
        contents += "\n" + blob.name        

    return contents, 200

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500
