"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 05 January, 2018 @ 3:11 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""


class NeuralNetwork:
    def __init__(self, **kwargs):
        self._logging = kwargs.get('logging', True)

    def fit(self, X, y):
        pass

    def score(self, X, y):
        pass

    def predict(self, X):
        pass

    def inference(self, X):
        self.predict(X)

    def save(self, filename):
        pass
