"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 04 January, 2018 @ 7:27 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import Flask

from helpers import config as cfg

app = Flask(cfg.APP_NAME)

# External routes/views
from views.projects import *
from views.research import *


@app.route('/')
def index():
    return render_template('index.html')
