"""
  @author Victor I. Afolabi
  
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 01 February, 2018 @ 2:39 PM.
  Copyright © 2018. Victor. All rights reserved.
"""

# This snippet is in public domain.
# However, please retain this link in your sources:
# http://flask.pocoo.org/snippets/120/
# Danya Alexeyevsky

from functools import wraps

from flask import session, redirect, current_app, request, url_for

from imaginary.server import app

with app.app_context():
    class Back(object):
        """To be used in views.

        Use `anchor` decorator to mark a view as a possible point of return.

        `url()` is the last saved url.

        Use `redirect` to return to the last return point visited.
        """

        cfg = current_app.config.get
        cookie = cfg('REDIRECT_BACK_COOKIE', 'back')
        default_view = cfg('REDIRECT_BACK_DEFAULT', 'index')

        @staticmethod
        def anchor(func, cookie=cookie):
            @wraps(func)
            def result(*args, **kwargs):
                session[cookie] = request.url
                return func(*args, **kwargs)

            return result

        @staticmethod
        def url(default=default_view, cookie=cookie):
            return session.get(cookie, url_for(default))

        @staticmethod
        def redirect(default=default_view, cookie=cookie):
            return redirect(back.url(default, cookie))


    back = Back()
