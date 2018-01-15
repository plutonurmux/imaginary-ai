"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 06 January, 2018 @ 12:57 AM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from models.config.base import Config, APP_NAME


class Production(Config):
    DATABASE_URI = f'mysql://victor@localhost/{APP_NAME}'


class Development(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True
