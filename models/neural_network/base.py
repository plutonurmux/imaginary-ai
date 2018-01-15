"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 05 January, 2018 @ 3:11 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from models.dataset.image import ImageDataset


class NeuralNetwork(object):

    def __init__(self, dataset, **kwargs):
        # Raise an error if dataset is not an instance of dataset
        if not isinstance(dataset, ImageDataset):
            raise TypeError('dataset must be an instance of models.dataset.Dataset class')
        self._dataset = dataset

        # Keyword arguments
        self._batch_size = kwargs.get('batch_size', 64)
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
