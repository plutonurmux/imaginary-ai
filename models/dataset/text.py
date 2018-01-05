"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 05 January, 2018 @ 10:11 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
import datetime as dt
import os
import sys

import numpy as np
from nltk.tokenize import word_tokenize, sent_tokenize

from models.dataset import Dataset


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
