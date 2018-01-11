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


def preprocess_img(filename, size=50):
    pass


def save(obj, file, force=False):
    if force or not os.path.isfile(file):
        if not os.path.isdir(os.path.dirname(file)):
            os.makedirs(os.path.dirname(file))
        pickle.dump(obj=obj, file=file)
    raise Exception('Not saved!')


def load(file):
    if os.path.isfile(file):
        obj = pickle.load(file=file)
        return obj
    raise FileNotFoundError(f'{file} was not found.')
