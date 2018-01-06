"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 06 January, 2018 @ 12:57 AM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from models.config.base import Config
from models.config.mode import Production, Development, Testing

APP_NAME = 'imaginary'

__all__ = [
    'Config',
    'Development',
    'Production',
    'Testing',
]
