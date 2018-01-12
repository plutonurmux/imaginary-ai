"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 05 January, 2018 @ 3:15 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
# import cv2
import os
import pickle

import keras.models


def preprocess_img(filename, size=50):
    print(f'Processing {filename}. size = {size}')
    pass


def save(obj, file, force=False):
    if force or not os.path.isfile(file):
        if not os.path.isdir(os.path.dirname(file)):
            os.makedirs(os.path.dirname(file))
        with open(file, mode='wb') as f:
            pickle.dump(obj=obj, file=f)
    raise Exception('Not saved!')


def load(file):
    if os.path.isfile(file):
        with open(file, mode='rb') as f:
            obj = pickle.load(file=f)
            return obj
    raise FileNotFoundError(f'{file} was not found.')


def load_model(path):
    return keras.models.load_model(filepath=path)
