"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 09 January, 2018 @ 1:15 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from models.neural_network.pre_trained import base
from models.neural_network.pre_trained.resnet import ResNet
from models.neural_network.pre_trained.inception import Inception
from models.neural_network.pre_trained.vgg import VGG16, VGG19

__all__ = [
    'Inception',
    'ResNet',
    'VGG16',
    'VGG19',
]
