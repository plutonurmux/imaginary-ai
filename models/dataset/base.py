"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 05 January, 2018 @ 10:07 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""

import os
import pickle
import sys
import tarfile
import urllib.request
import zipfile

import numpy as np


class Dataset(object):
    """
    Dataset pre-processing base class

    :param data_dir:
        top level directory where data resides

    :param kwargs:
        `logging`: Feedback on background metrics
    """

    def __init__(self, data_dir, **kwargs):
        self._data_dir = data_dir
        # Keyword arguments
        self._logging = kwargs['logging'] if 'logging' in kwargs else True
        # Features and labels
        self._X = np.array([])
        self._y = np.array([])
        # Computed for self.next_batch
        self._num_examples = 0
        self._epochs_completed = 0
        self._index_in_epoch = 0

    def create(self):
        """Create datasets"""
        self._process()
        self._num_examples = self._X.shape[0]

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
        dirs = save_file.split('/')
        if len(dirs) > 1 and not os.path.isdir('/'.join(dirs[:-1])):
            os.makedirs('/'.join(dirs[:-1]))
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

    def maybe_download_and_extract(self, url, download_dir='downloads', force=False):
        """
        Download and extract the data if it doesn't already exist.
        Assumes the url is a tar-ball file.

        :param url:
            Internet URL for the tar-file to download.
            Example: "http://nlp.stanford.edu/data/glove.6B.zip"

        :param download_dir:
            Directory to download files.
            Example: "datasets/GloVe/"

        :param force: boolean default False
            Force download even if the file already exists.

        :return:
            Nothing.
        """

        # Filename for saving the file downloaded from the internet.
        # Use the filename from the URL and add it to the download_dir.
        filename = url.split('/')[-1]
        file_path = os.path.join(self._data_dir, filename)

        # Check if the file already exists.
        # If it exists then we assume it has also been extracted,
        # otherwise we need to download and extract it now.
        if not os.path.exists(file_path) or force:
            # Check if the download directory exists, otherwise create it.
            if not os.path.exists(self._data_dir):
                os.makedirs(self._data_dir)

            # Download the file from the internet.
            file_path, _ = urllib.request.urlretrieve(url=url,
                                                      filename=file_path,
                                                      reporthook=self._print_download_progress)

            print()
            print("Download finished. Extracting files.")

            if file_path.endswith(".zip"):
                # Unpack the zip-file.
                zipfile.ZipFile(file=file_path, mode="r").extractall(
                    download_dir)
            elif file_path.endswith((".tar.gz", ".tgz")):
                # Unpack the tar-ball.
                tarfile.open(name=file_path, mode="r:gz").extractall(
                    download_dir)

            print("Done.")
        else:
            print("Data has apparently already been downloaded and unpacked.")

    def next_batch(self, batch_size, shuffle=True):
        """
        Get the next batch in the dataset

        :param batch_size: int
            Number of batches to be retrieved

        :param shuffle: bool
            Randomly shuffle the batches returned

        :return:
            Returns `batch_size` batches
            features - np.array([batch_size, ?])
            labels   - np.array([batch_size, ?])
        """
        start = self._index_in_epoch
        # Shuffle for first epoch
        if self._epochs_completed == 0 and start == 0 and shuffle:
            permute = np.arange(self._num_examples)
            np.random.shuffle(permute)
            self._X = self._X[permute]
            self._y = self._y[permute]
        # Go to next batch
        if start + batch_size > self._num_examples:
            # Finished epoch
            self._epochs_completed += 1
            # Get the rest examples in this epoch
            rest_examples = self._num_examples - start
            rest_features = self._X[start:self._num_examples]
            rest_labels = self._y[start:self._num_examples]
            # Shuffle the data
            if shuffle:
                permute = np.arange(self._num_examples)
                np.random.shuffle(permute)
                self._X = self._X[permute]
                self._y = self._y[permute]
            # Start next epoch
            start = 0
            self._index_in_epoch = batch_size - rest_examples
            end = self._index_in_epoch
            features = np.concatenate(
                (rest_features, self._X[start:end]), axis=0)
            labels = np.concatenate((rest_labels, self._y[start:end]), axis=0)
            return features, labels
        else:
            self._index_in_epoch += batch_size
            end = self._index_in_epoch
            return self._X[start:end], self._y[start:end]

    def train_test_split(self, test_size=0.1, **kwargs):
        """
        Splits dataset into training and testing set.

        :param test_size: float, default 0.1
                    Size of the testing data in %.
                    Default is 0.1 or 10% of the dataset.

        :keyword valid_portion: float, None, default
                    Size of validation set in %.
                    This will be taking from training set
                    after splitting into training and testing set.

        :return:
            np.array of [train_X, train_y, test_X, test_y] if
            `valid_portion` is not set
            or
            np.array of [train_X, train_y, test_X, test_y, val_X, val_y] if
            `valid_portion` is set
        """
        test_size = int(len(self._X) * test_size)

        train_X = self._X[:-test_size]
        train_y = self._y[:-test_size]
        test_X = self._X[-test_size:]
        test_y = self._y[-test_size:]

        if 'valid_portion' in kwargs:
            valid_portion = kwargs['valid_portion']
            valid_portion = int(len(train_X) * valid_portion)

            train_X = train_X[:-valid_portion]
            train_y = train_y[:-valid_portion]
            val_X = train_X[-valid_portion:]
            val_y = train_y[-valid_portion:]
            return np.array([train_X, train_y, test_X, test_y, val_X, val_y])

        return np.array([train_X, train_y, test_X, test_y])

    @property
    def data_dir(self):
        return self._data_dir

    @property
    def features(self):
        return self._X

    @property
    def labels(self):
        return self._y

    @property
    def num_examples(self):
        return self._num_examples

    @property
    def index_in_epoch(self):
        return self._index_in_epoch

    @property
    def num_classes(self):
        return self._y.shape[-1]

    @property
    def epochs_completed(self):
        return self._epochs_completed

    def _process(self):
        pass

    def _one_hot(self, arr):
        arr, uniques = list(arr), list(set(arr))
        encoding = np.zeros(shape=[len(arr), len(uniques)], dtype=np.int32)
        for i, a in enumerate(arr):
            encoding[i, uniques.index(a)] = 1.
        return encoding

    @staticmethod
    def _print_download_progress(count, block_size, total_size):
        # Percentage completion.
        pct_complete = float(count * block_size) / total_size
        # Status-message. Note the \r which means the line should overwrite itself.
        msg = f"\r\t- Download progress: {pct_complete:.2%}"
        # Print it.
        sys.stdout.write(msg)
        sys.stdout.flush()
