import logging

from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500