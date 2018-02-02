"""
  @author Victor I. Afolabi
  
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 01 February, 2018 @ 11:44 PM.
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import render_template

from imaginary.server import app, back


@app.route('/research/')
@back.anchor
def research():
    """
    Research home.

    :return: HTML template.
    """
    return render_template('research/index.html')


@app.route('/research/a-language-model/')
def a_language_model():
    """
    A Language model research page.

    :return: HTML template.
    """
    return render_template('research/a-language-model.html')
