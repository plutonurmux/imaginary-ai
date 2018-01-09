"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 09 January, 2018 @ 1:15 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""


class PreTrained:
    def __init__(self, **kwargs):
        self._weights = kwargs.get('weight', 'imagenet')

    def predict(self, path):
        pass
