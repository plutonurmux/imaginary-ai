"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 05 January, 2018 @ 10:08 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
import os
import sys

import numpy as np

from models.dataset import Dataset


################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | ImageDataset
# |     for image datasets
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################

class ImageDataset(Dataset):
    """
    Dataset subclass for pre-processing image data

    :param data_dir: str

    :param size: int default 50
        Size of the image. The image will be resize
        into (size, size). Resizing the image doesn't affect the
        image channels but it does affect the shape of the image.

    :param grayscale: bool default False
        Maybe convert the image to grayscale.
        Note: the image channel will be 1 if converted to grayscale.

    :param flatten: bool default True
        Maybe flatten the image into a 1-D array. The `features`
        shape will be moodified into (n, d) where n is `num_examples`
        and d in the flattened dimension.

    :param kwargs:
    """

    def __init__(self, size=50, grayscale=False, flatten=True, **kwargs):
        super().__init__(**kwargs)
        self.size = size
        self.grayscale = grayscale
        self.flatten = flatten

        self._labels = [l for l in os.listdir(
            self._data_dir) if l[0] is not '.']
        try:
            from PIL import Image
        except Exception as e:
            raise ModuleNotFoundError(f'{e}')
        # First image
        img_dir = os.path.join(self._data_dir, self._labels[0])
        img_file = os.path.join(img_dir, os.listdir(img_dir)[1])
        img = self.__create_image(img_file, return_obj=True)
        self._channel = img.im.bands
        # free memory
        del img_dir
        del img_file
        del img

    @property
    def images(self):
        return self._X

    @property
    def channel(self):
        return self._channel

    def _process(self):
        img_dirs = [os.path.join(self._data_dir, l) for l in self._labels]
        total_images = sum([len(os.listdir(d)) for d in img_dirs])
        if self.flatten:
            self._X = np.zeros(
                shape=[total_images, self.size * self.size * self.channel])
        else:
            self._X = np.zeros(
                shape=[total_images, self.size, self.size, self.channel])
        self._y = np.zeros(shape=[total_images, len(self._labels)])
        # Free memory
        del total_images
        del img_dirs
        counter = 0
        for i, label in enumerate(self._labels):
            image_dir = os.path.join(self._data_dir, label)
            image_list = [d for d in os.listdir(image_dir) if d[0] is not '.']
            for j, file in enumerate(image_list):
                # noinspection PyBroadException
                try:
                    image_file = os.path.join(image_dir, file)
                    img = self.__create_image(image_file)
                    hot_label = self.__create_label(label)
                    self._X[counter, :] = img
                    self._y[counter, :] = hot_label
                except Exception as e:
                    sys.stderr.write(f'\r{i} - {e}')
                    sys.stderr.flush()
                finally:
                    counter += 1
                if self._logging:
                    sys.stdout.write(f'\rProcessing {i+1:,} of {len(self._labels):,} class labels'
                                     f'\t{j+1:,} of {len(image_list):,} images')
        # Free up memory
        del counter

    def __create_image(self, file, return_obj=False):
        try:
            from PIL import Image
        except Exception as e:
            raise ModuleNotFoundError(f'{e}')
        img = Image.open(file)
        img = img.resize((self.size, self.size))
        if self.grayscale:
            img = img.convert('L')
        if return_obj:
            return img
        # convert to np.array
        img = np.array(img, dtype=np.float32)
        if self.flatten:
            img = img.flatten()
        return img

    def __create_label(self, label):
        hot = np.zeros(shape=[len(self._labels)], dtype=int)
        hot[self._labels.index(label)] = 1
        return hot
