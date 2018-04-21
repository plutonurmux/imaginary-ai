"""
  @author Victor I. Afolabi

  A.I. Engineer & Software developer
  javafolabi@gmail.com

  Created on 01 February, 2018 @ 2:38 PM.
  Copyright (c) 2018. Victor. All rights reserved.
"""
from flask import Flask
from config import Development
from settings import STATIC_FOLDER, TEMPLATE_FOLDER


app = Flask(__name__,
            static_folder=STATIC_FOLDER,
            template_folder=TEMPLATE_FOLDER)
app.config.from_object(Development)
