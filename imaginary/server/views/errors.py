"""
  @author Victor I. Afolabi
  
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 01 February, 2018 @ 2:39 PM.
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import render_template

from imaginary.server import app, back


@app.errorhandler(400)
def bad_request(error):
    return render_template('errors/400.html', error=error, back=back), 400


@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html', error=error, back=back), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', error=error, back=back), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('errors/405.html', error=error, back=back), 405


@app.errorhandler(500)
def internal_server(error):
    return render_template('errors/500.html', error=error, back=back), 500
