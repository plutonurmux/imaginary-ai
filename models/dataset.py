"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 05 January, 2018 @ 10:03 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com

  Created on 02 November, 2017 @ 11:24 PM.

  Copyright © 2017. Victor. All rights reserved.
"""
import datetime as dt
import os
import pickle
import sys
import tarfile
import urllib.request
import zipfile

import numpy as np
from nltk.tokenize import word_tokenize, sent_tokenize


################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Dataset
# |     base dataset class.
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
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
                    sys.stderr.write(f'{e}')
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


################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | TextDataset
# |     for textual dataset
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
class TextDataset(Dataset):
    """
    Dataset subclass for pre-processing textual data

    :param data_dir: str

    :param window: int
        is the maximum distance between the current and predicted
        word within a sentence

    :param max_word: int
        Maximum number of words to be kept

    :param kwargs:
    """

    def __init__(self, window=2, max_word=None, **kwargs):
        super().__init__(**kwargs)
        self._window = window
        self._max_word = max_word

        # TODO: Look into `data_dir`. You may wanna get all files in there and read as a BIG corpus
        corpus_text = open(self._data_dir, mode='r', encoding='utf-8').read()
        if self._max_word:
            corpus_text = corpus_text[:self._max_word]
        corpus_text = corpus_text.lower()
        try:
            from nltk import word_tokenize, sent_tokenize
        except Exception as e:
            raise ModuleNotFoundError(f'{e}')
        # word2id & id2word
        unique_words = set(word_tokenize(corpus_text))
        self._vocab_size = len(unique_words)
        self._word2id = {w: i for i, w in enumerate(unique_words)}
        self._id2word = {i: w for i, w in enumerate(unique_words)}

        # Sentences
        raw_sentences = sent_tokenize(corpus_text)
        self._sentences = [word_tokenize(sent) for sent in raw_sentences]

        # Free some memory
        del corpus_text
        del unique_words
        del raw_sentences

    @property
    def vocab_size(self):
        return self._vocab_size

    @property
    def word2id(self):
        return self._word2id

    @property
    def id2word(self):
        return self._id2word

    @property
    def sentences(self):
        return self._sentences

    def _process(self):
        # Creating features & labels
        self._X = np.zeros(shape=[len(self._sentences), self._vocab_size])
        self._y = np.zeros(shape=[len(self._sentences), self._vocab_size])

        start_time = dt.datetime.now()
        for s, sent in enumerate(self._sentences):
            for i, word in enumerate(sent):
                start = max(i - self._window, 0)
                end = min(self._window + i, len(sent)) + 1
                word_window = sent[start:end]
                for context in word_window:
                    if context is not word:
                        self._X[s] = self._one_hot(self._word2id[word])
                        self._y[s] = self._one_hot(self._word2id[context])
            if self._logging:
                sys.stdout.write(
                    f'\rProcessing {s+1:,} of {len(self._sentences):,} sentences.'
                    f'\tTime taken: {dt.datetime.now() - start_time}')
        # Free memory
        del start_time

    def _one_hot(self, idx):
        temp = np.zeros(shape=[self._vocab_size])
        temp[idx] = 1.
        return temp


################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | WordVectorization
# |     for vectoring word dataset
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
class WordVectorization(Dataset):
    """
    Dataset subclass for pre-processing textual data

    :param data_dir: str
        Dataset directory.

    :param size: str default 'sm'
        size of GloVe dimension to be used.
        'sm' => Small file containing 50-D
        'md' => Medium file containing 100-D
        'lg' => Large file containing 200-D
        'xl' => Extra large file containing 300-D

    :param kwargs:
    """

    def __init__(self, corpus, size='sm', **kwargs):
        super().__init__(**kwargs)
        self._corpus = corpus
        self._size = size
        self._glove_url = 'http://nlp.stanford.edu/data/glove.6B.zip'
        self._glove_dir = '.'.join(
            self._glove_url.split('/')[-1].split('.')[:-1])
        self._glove_dir = os.path.join(self._data_dir, self._glove_dir)

        sizes = ['sm', 'md', 'lg', 'xl']
        GLOVE_FILES = [os.path.join(self._glove_dir, 'glove.6B.50d.txt'),
                       os.path.join(self._glove_dir, 'glove.6B.100d.txt'),
                       os.path.join(self._glove_dir, 'glove.6B.200d.txt'),
                       os.path.join(self._glove_dir, 'glove.6B.300d.txt')]
        if self._size not in sizes:
            msg = "`size` attribute includes: 'sm', 'md', 'lg', 'xl' " \
                  "for small, medium, large & extra-large respectively "
            raise ValueError(msg)
        index = sizes.index(self._size)
        self._glove_file = GLOVE_FILES[index]

        self._glove_vector = {}
        self._sentence_words = []

        # maybe download & extract file
        if not os.path.isfile(self._glove_file):
            confirm = input('Download glove file, 862MB? Y/n: ')
            if 'y' in confirm.lower():
                self.maybe_download_and_extract(
                    self._glove_url, download_dir=self._glove_dir, force=True)
            else:
                sys.stderr.write('Access denied! Download file to continue...')
                sys.stderr.flush()
                raise FileNotFoundError(
                    f'{self.glove_file} was not found. Download file to continue...')
        else:
            print(
                f'Apparently, `{self._glove_file}` has been downloaded and extracted.')

    def _process(self):
        # load GloVe word vectors
        self._load_glove()
        # Read dataset file(s)
        # sentence tokenize contents
        sentences = sent_tokenize(self._corpus)
        for i, sent in enumerate(sentences):
            vector, words = self._sent2seq(sent)
            if i == 0:
                self._X = np.copy(vector)
            else:
                self._X = np.concatenate((self._X, vector), axis=0)
            self._sentence_words.append(words)
            if self._logging:
                sys.stdout.write(f'\rProcessing {i+1:,} of {len(sentences):,} sentences..')
                sys.stdout.flush()
        # convert sentences to vectors
        # add to word vectors to features

    def _lookup(self, vector):
        # Check for the word for the corresponding vector
        pass

    def _sent2seq(self, sentence):
        tokens = word_tokenize(sentence)
        vectors = []
        words = []
        for token in tokens:
            # noinspection PyBroadException
            try:
                vector = self._glove_vector[token.lower()]
            except Exception as e:
                vector = self._glove_vector['unk']
                sys.stderr.write(f'\r{e}')
                sys.stderr.flush()
            vectors.append(vector)
            words.append(token)
        return np.asarray(vectors), words

    def _visualize(self, sentence):
        import matplotlib.pyplot as plt
        import matplotlib.ticker as ticker

        vectors, words = self._sent2seq(sentence)
        mat = np.vstack(vectors)

        fig = plt.figure()
        ax = fig.add_subplot(111)
        shown = ax.matshow(mat, aspect='auto')
        ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
        fig.colorbar(shown)

        ax.set_yticklabels([''] + words)
        plt.show()

    def _load_glove(self):
        with open(self._glove_file, mode='r', encoding='utf-8') as glove:
            lines = glove.readlines()
            for i, line in enumerate(lines):
                name, vector = line.split(' ', 1)
                self._glove_vector[name] = np.fromstring(vector, sep=' ')
                if self._logging:
                    sys.stdout.write(f'\rLoading {i+1:,} of {len(lines):,}')
        return

    @property
    def glove_dir(self):
        return self._glove_dir

    @property
    def glove_file(self):
        return self._glove_file

    @property
    def glove_vector(self):
        return self._glove_vector


if __name__ == '__main__':
    data_dir = 'datasets/flowers'
    save_file = 'datasets/saved/features-{0}x{0}.pkl'

    data = ImageDataset(data_dir=data_dir)
    data.create()  # creates features & label
    data.save(save_file.format(data.size))  # saves this object
    # data = data.load(save_file.format(data.size))  # loads saved object

    # Split into training, testing & validation set.
    X_train, y_train, X_test, y_test, X_val, y_val = data.train_test_split(
        test_size=0.2, valid_portion=0.1)
    # X_train, y_train, X_test, y_test = data.train_test_split(test_size=0.2)

    print(f'\nTrain: X{X_train.shape}\tTest: y{y_test.shape}\tValid: X{X_val.shape}')
