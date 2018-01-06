"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 06 January, 2018 @ 12:57 AM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from passlib.hash import sha256_crypt

# from models import config as cfg


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = sha256_crypt.encrypt('Imaginary A.I.')
    # Flask Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'javafolabi@gmail.com'
    MAIL_PASSWORD = 'itsprivate'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
