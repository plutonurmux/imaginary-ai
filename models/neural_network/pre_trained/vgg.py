"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 09 January, 2018 @ 1:17 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
import numpy as np
from keras.applications import vgg16, vgg19
from keras.applications.vgg16 import preprocess_input, decode_predictions
from keras.preprocessing import image

from models.neural_network.pre_trained.base import PreTrained


class VGG16(PreTrained):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = kwargs.get('size', 224)
        self._model = vgg16.VGG16(weights=self._weights)

    def predict(self, path, top=5):
        img = image.load_img(path, target_size=(self.size, self.size))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        pred = self._model.predict(x)
        pred = decode_predictions(pred, top=top)[0]
        return pred


class VGG19(PreTrained):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = kwargs.get('size', 224)
        self._model = vgg19.VGG19(weights=self._weights)

    def predict(self, path, top=5):
        img = image.load_img(path, target_size=(self.size, self.size))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        pred = self._model.predict(x)
        pred = decode_predictions(pred, top=top)[0]
        return pred
