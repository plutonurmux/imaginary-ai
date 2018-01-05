"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 05 January, 2018 @ 11:55 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import render_template

from views import app


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error/404.html', error=error), 404


@app.errorhandler(403)
def forbidden(error):
    return render_template('error/403.html', error=error), 403


@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('error/405.html', error=error), 405


@app.errorhandler(500)
def internal_server(error):
    return render_template('error/500.html', error=error), 500
