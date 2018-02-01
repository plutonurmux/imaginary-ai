"""
  @author Victor I. Afolabi
  
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 01 February, 2018 @ 2:39 PM.
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import redirect, url_for

from imaginary.server import app


@app.route('/_contact', methods=['POST'])
def contact_form():
    """
    Contact form API.

    :return: redirect to index
    """
    return redirect(url_for('index'))
