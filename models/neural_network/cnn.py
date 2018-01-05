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


class ConvolutionalNeuralNetwork(NeuralNetwork):

    # TODO: Correct the parameters
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = Sequential()

        # keyword arguments
        self._num_classes = 10
        self.filters = kwargs.get('filters', [16, 32])
        self._fully_connected = kwargs.get('fully_connected', [1024])
        self.batch_size = 24

        self.kernel_size = kwargs.get('kernel_size', 5)
        self._img_size = kwargs.get('img_size', 50)
        self._img_channel = kwargs.get('img_channel', 3)
        self._img_shape = [self._img_size, self._img_size, self._img_channel]

    def fit(self, X, y):
        # Input layer
        self.model.add(InputLayer(input_shape=np.prod(self._img_shape)))
        self.model.add(Reshape(target_shape=self._img_shape))
        # Convolutional Layers
        for i, f in enumerate(self.filters):
            self.model.add(Conv2D(filters=f, kernel_size=self.kernel_size,
                                  padding='same', activation='relu', name=f'layer_conv{i}'))
            self.model.add(MaxPooling2D(strides=2, padding='same'))
        # flatten layer
        self.model.add(Flatten())
        # Fully Connected Layers
        for i, fc in enumerate(self._fully_connected):
            self.model.add(Dense(units=fc, activation='relu', name=f'layer_fc{i}'))
        # Output layer
        self.model.add(Dense(units=self._num_classes, activation='softmax'))

        # Compilation
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        # Training
        self.model.fit(x=X, y=y, epochs=1, batch_size=self.batch_size)
        return self.model

    def predict(self, X):
        y_pred = self.model.predict(x=X)
        cls_pred = np.argmax(y_pred, axis=1)
        return y_pred, cls_pred
