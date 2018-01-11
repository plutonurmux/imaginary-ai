"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 09 January, 2018 @ 2:04 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
import numpy as np
from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_v3 import preprocess_input, decode_predictions
from keras.preprocessing import image

from helpers.consts import PRE_TRAINED_MODELS
from models.neural_network.pre_trained.base import PreTrained
from models.neural_network.utils import save


class Inception(PreTrained):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = kwargs.get('size', 224)
        self._model = InceptionV3(weights=self._weights)

    def predict(self, path, top=5):
        img = image.load_img(path, target_size=(self.size, self.size))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        pred = self._model.predict(x)
        pred = decode_predictions(pred, top=top)[0]
        return pred


if __name__ == '__main__':
    model = Inception(weight='imagenet')
    save(model, PRE_TRAINED_MODELS['INCEPTION'])
    print('Saved')
