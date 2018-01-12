"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 06 January, 2018 @ 7:54 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
import os

PROJECT_DIR = os.getcwd()

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Saved models directories
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
MODEL_DIR = os.path.join(PROJECT_DIR, 'models')
SAVED_MODEL_DIR = os.path.join(MODEL_DIR, 'saved')
PRE_TRAINED_DIR = os.path.join(SAVED_MODEL_DIR, 'pre-trained')

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Static files directories
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
STATIC_DIR = os.path.join(PROJECT_DIR, 'static')
DATASETS_DIR = os.path.join(STATIC_DIR, 'datasets')
UPLOAD_DIR = os.path.join(STATIC_DIR, 'images/uploads')


################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Pre-trained models filepath
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
PRE_TRAINED_MODELS = {
    'INCEPTION': os.path.join(PRE_TRAINED_DIR, 'inception.model'),
    'RESNET': os.path.join(PRE_TRAINED_DIR, 'resnet.model'),
}

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
