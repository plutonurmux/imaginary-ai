"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 07 January, 2018 @ 7:27 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
import os.path

# import models.neural_network.pre_trained as pre_trained
# import models.projects as projects
# TODO: Fix this code leak. This is where keras is imported automatically when project starts
from models.neural_network.pre_trained.inception import Inception
from models.projects.utils import maybe_download_or_upload
from models.projects.search import Search
from helpers.consts import STATIC_DIR


def process(request):
    try:
        # Upload image.
        image_path = upload(request)

        # Classify image.
        predictions = predict(image_path, top=5)

        # Search top prediction label
        # s = predictions['top']['label']
        # print(f'Searching for {s}')
        # search_results = search(s)

        return {
            'image_path': image_path,
            'predictions': predictions,
            # 'search_results': search_results
        }
    except Exception as e:
        raise Exception(e)


def upload(request):
    image = None
    if 'upload-file' not in request.form:
        image = {'file': request.files['upload-file'], 'type': 'upload'}
    elif 'camera-file' not in request.form:
        image = {'file': request.files['camera-file'], 'type': 'upload'}
    elif request.form['image-url']:
        image = {'file': request.form['image-url'], 'type': 'url'}
    path = maybe_download_or_upload(image, folder='')
    if path and type(path) == str:
        return path
    else:
        raise Exception('Trouble uploading image')


def predict(path, top=5):
    """
    Predicts what class an image input belongs to using the imagenet
    pre-trained weights.

    :param path: str,
        Image path relative to the static directory
        e.g.
        >>> path = 'images/uploads/elephant.jpg'
        >>> results = model.predict(path=path, top=3)

    :param top: int,
        How many class predictions to be returned.

    :return: results, dict
        Results containing to items: top prediction & all predictions
        top prediction contains a dictionary of the score and label.
        all predictions is a dictionary of labels and scores of `top`
        number of classes.

        e.g.
        >>> results['top']
        >>> # {'label': 'african_elephant', 'score': 0.832}
        >>> results['all']
        >>> # {'african_elephant': 0.832, 'zambia_elephant': 0.132, ...}
    """
    print('Loading pre-trained inception model...')
    # Full/absolute image path
    full_img_path = os.path.join(STATIC_DIR, path)

    # Loading the a pre-trained InceptionV3 model.
    model = Inception(weights='imagenet')

    # Predict the image label.
    pred = model.predict(full_img_path, top=top)

    # Clean up predictions
    pred = list(map(_predict_pprint, pred))

    # Top prediction's labels and their scores
    top_label = pred[0][0]
    top_score = pred[0][1]

    return {
        'top': {'label': top_label, 'score': top_score},
        'all': dict(pred)
    }


def search(prediction):
    search = Search()
    results = search.search(prediction)
    return results


def _predict_pprint(label_score):
    # label_score[0] = imagenet class id
    label = label_score[1]
    score = f'{label_score[2]:.2%}'
    label = label.replace('_', ' ').capitalize()
    return label, score
