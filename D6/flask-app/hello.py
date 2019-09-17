#!/usr/bin/python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hello():
    return 'Hello there'

@app.route('/about_page')
def About():
    return 'About page'

@app.route('/contat_page')
def Contact():
    return 'Contact'




#spustenie: set FLASK_APP=nazov_suboru.py // flask run
