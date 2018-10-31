import json
import logging
import os
import pickle

from flask import Flask, request
import cloudstorage as gcs
from google.cloud import storage
from google.appengine.api import app_identity
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import webapp2

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    print ("WORKING")
    return "Hello World", 200

@app.route('/bucket', methods=['GET'])
def bucket():
    storage_client = storage.Client()
    bucket_name = app_identity.get_default_gcs_bucket_name()
    bucket = storage_client.get_bucket(bucket_name)

    blobs = bucket.list_blobs()

    for blob in blobs:
        print(blob.name)
   
    return bucket_name, 200

@app.route('/predict', methods=['POST'])
def predict():
   return "Predict", 200

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500
