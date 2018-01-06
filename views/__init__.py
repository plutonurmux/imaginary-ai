"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 04 January, 2018 @ 7:27 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import Flask

app = Flask('__main__')
app.config.from_object('models.config.Development')

# Helper
from helpers import back
# External routes/views
from views.error import *
from views.pages import *
from views.projects import *
from views.research import *


@app.route('/')
@back.anchor
def index():
    return render_template('index.html')


@app.route('/elements/')
def elements():
    return render_template('elements.html')
