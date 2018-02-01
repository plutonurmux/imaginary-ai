"""
  @author Victor I. Afolabi
  
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 01 February, 2018 @ 11:43 PM.
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import render_template

from imaginary.server import app, back


@app.route('/projects/')
@back.anchor
def projects():
    return render_template('projects/index.html')
