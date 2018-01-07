"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 06 January, 2018 @ 7:54 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
import os


PROJECT_DIR = os.getcwd()
STATIC_DIR = os.path.join(PROJECT_DIR, 'static')
DATASETS_DIR = os.path.join(STATIC_DIR, 'datasets')
UPLOAD_DIR = os.path.join(STATIC_DIR, 'images/uploads')

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
