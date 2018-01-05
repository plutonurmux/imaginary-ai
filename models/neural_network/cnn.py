"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 05 January, 2018 @ 3:09 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""

from models.neural_network.base import NeuralNetwork


class ConvolutionalNeuralNetwork(NeuralNetwork):

    def __init__(self, layers, **kwargs):
        super().__init__(**kwargs)
        self.layers = layers
