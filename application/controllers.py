"""
  @author Victor I. Afolabi

  A.I. Engineer & Software developer
  javafolabi@gmail.com

  Created on 01 February, 2018 @ 2:39 PM.
  Copyright (c) 2018. Victor. All rights reserved.
"""
from flask import render_template

from application import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<path:path>', methods=['GET'])
def paths(path):
    return render_template('index.html')
