"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 05 January, 2018 @ 3:09 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""

import numpy as np
from keras.layers import Conv2D, Dense, Flatten
from keras.layers import InputLayer
from keras.layers import Reshape, MaxPooling2D
from keras.models import Sequential

from models.neural_network.base import NeuralNetwork


class CNN(NeuralNetwork):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._model = Sequential()

        # keyword arguments
        self.kernel_size = kwargs.get('kernel_size', 5)
        self.filters = kwargs.get('filters', [16, 32])
        self.dense = kwargs.get('dense', [512, 1024])

        # Input parameters
        self._img_size = self._dataset.size
        self._img_channel = self._dataset.channel
        self._img_shape = [self._img_size, self._img_size, self._img_channel]
        self._img_size_flat = self._img_size * self._img_size * self._img_channel
        # self._img_size_flat = np.prod(self._img_shape)

    def fit(self, X, y, epochs=5):
        # Input layer
        self._model.add(InputLayer(input_shape=[self._img_size_flat]))
        self._model.add(Reshape(target_shape=self._img_shape))
        # Convolutional Layers
        for i, f in enumerate(self.filters):
            self._model.add(Conv2D(filters=f, kernel_size=self.kernel_size,
                                   padding='same', activation='relu', name=f'layer_conv{i}'))
            self._model.add(MaxPooling2D(strides=2, padding='same'))
        # flatten layer
        self._model.add(Flatten())
        # Fully Connected Layers
        for i, fc in enumerate(self.dense):
            self._model.add(Dense(units=fc, activation='relu', name=f'layer_fc{i}'))
        # Output layer
        self._model.add(Dense(units=self._dataset.num_classes, activation='softmax'))

        # Compilation
        self._model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        # Training
        self._model.fit(x=X, y=y, epochs=epochs, batch_size=self._batch_size)
        return self._model

    def predict(self, X):
        y_pred = self._model.predict(x=X)
        cls_pred = np.argmax(y_pred, axis=1)
        return y_pred, cls_pred

    def score(self, X, y):
        result = self._model.evaluate(x=X, y=y)
        # {'loss': 0.550, 'acc': 0.9821}
        return dict(zip(self._model.metrics_names, result))

    def save(self, filename):
        pass
