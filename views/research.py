"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 04 January, 2018 @ 7:32 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import render_template

from views import app


@app.route('/research/')
def research():
    return render_template('research/index.html')


@app.route('/research/a-language-model/')
def a_language_model():
    return render_template('research/a-language-model.html')
