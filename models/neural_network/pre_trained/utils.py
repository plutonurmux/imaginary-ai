"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 12 January, 2018 @ 1:14 AM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from keras.models import load_model


def load(path):
    model = load_model(filepath=path)
    return model
