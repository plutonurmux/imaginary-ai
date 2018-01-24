"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 04 January, 2018 @ 7:32 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import render_template

from views import app, back


@app.route('/research/')
@back.anchor
def research():
    """Research page.

    Decorators:
        back
        app

    Returns:
        [render_template] -- [/research/ html template.]
    """

    return render_template('research/index.html')


@app.route('/research/a-language-model/')
@back.anchor
def a_language_model():
    """A language model research page.

    Decorators:
        back
        app

    Returns:
        [render_template] -- [/research/a-langauge-model.html template.]
    """

    return render_template('research/a-language-model.html')
