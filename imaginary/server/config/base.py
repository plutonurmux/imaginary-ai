"""
  @author Victor I. Afolabi
  
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 01 February, 2018 @ 2:40 PM.
  Copyright © 2018. Victor. All rights reserved.
"""
from passlib.hash import sha256_crypt

from imaginary.settings import APP_NAME


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = sha256_crypt.encrypt(APP_NAME)
