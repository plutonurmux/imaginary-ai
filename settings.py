"""
  @author Victor I. Afolabi
  
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 01 February, 2018 @ 2:36 PM.
  Copyright © 2018. Victor. All rights reserved.
"""

import os


PROJECT_DIR = os.getcwd()
APP_NAME = os.path.basename(PROJECT_DIR)


STATIC_FOLDER = os.path.join(PROJECT_DIR, 'static')
TEMPLATE_FOLDER = os.path.join(PROJECT_DIR, 'templates')
