"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 06 January, 2018 @ 7:51 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""

import random

# Contains helper models for `/projects/image-classification/`
from helpers.consts import *


def __list_dir(directory, full_path=True):
    return [os.path.join(directory, d) if full_path else d
            for d in os.listdir(directory) if d[0] != '.']


def __get_random_image(class_path):
    image_paths = __list_dir(class_path, full_path=True)
    return image_paths[random.randrange(0, len(image_paths))]


def all_datasets(full_path=False):
    return __list_dir(DATASETS_DIR, full_path=full_path)


def dataset_classes(dataset_dir, full_path=False):
    return __list_dir(dataset_dir, full_path=full_path)


# {'anchor': '/path/to/anchor.jpg', ..., 'barrel': 'path/to/barrel.jpg'}
def classes_and_image(dataset_dir):
    ds_classes = dataset_classes(dataset_dir, full_path=True)
    # one_random_image = [img for img in __get_random_image(ds_classes)]
    one_random_image = [__get_random_image(cls) for cls in ds_classes]
    # Just the basename
    ds_classes = [os.path.basename(dc) for dc in ds_classes]
    ret_dict = dict(zip(ds_classes, one_random_image))
    return ret_dict
