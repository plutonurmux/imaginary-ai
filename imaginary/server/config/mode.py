"""
  @author Victor I. Afolabi
  
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 01 February, 2018 @ 2:40 PM.
  Copyright © 2018. Victor. All rights reserved.
"""
from imaginary.server.config.base import Config, APP_NAME


class Production(Config):
    DATABASE_URI = f'mysql://victor@localhost/{APP_NAME}'


class Development(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True
