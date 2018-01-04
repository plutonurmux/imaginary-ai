"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 04 January, 2018 @ 4:59 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import Flask, render_template

import helpers.config as cfg

app = Flask(cfg.APP_NAME)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/landing/')
def landing():
    return render_template('landing.html')


@app.route('/elements/')
def elements():
    return render_template('elements.html')


@app.route('/generic/')
def generic():
    return render_template('generic.html')
