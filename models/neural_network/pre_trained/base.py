"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 09 January, 2018 @ 1:15 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
import os
import pickle


class PreTrained:
    def __init__(self, **kwargs):
        self._weights = kwargs.get('weight', 'imagenet')

    def predict(self, path):
        pass

    def save(self, save_file, force=False):
        """
        Saves the dataset object

        :param save_file: str
            path to a pickle file

        :param force: bool
            force saving
        """
        if os.path.isfile(save_file) and not force:
            raise FileExistsError(
                f'{save_file} already exist. Set `force=True` to override.')
        save_dir = os.path.dirname(save_file)
        if not os.path.isdir(save_dir):
            os.makedirs(save_dir)
        with open(save_file, mode='wb') as f:
            pickle.dump(self, f)

    def load(self, save_file):
        """
        Load a saved Dataset object

        :param save_file:
            path to a pickle file

        :return: obj:
            saved instance of Dataset
        """
        if not os.path.isfile(save_file):
            raise FileNotFoundError(f'{save_file} was not found.')
        with open(save_file, 'rb') as f:
            # noinspection PyMethodFirstArgAssignment
            self = pickle.load(file=f)
        return self
