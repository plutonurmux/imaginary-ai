"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 07 January, 2018 @ 7:27 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from models.neural_network.pre_trained import Inception
from models.projects.search import Search
from models.projects.utils import maybe_download_or_upload


def process(request):
    try:
        # Upload image
        path = upload(request)
        print('Upload success!', path)
        # Classify image
        pred = predict(path)
        print('Classify success!', pred)
        # Search image
        # s = list(pred.keys())[0]
        # results = search(s)
        # print('Search success!', results)

        return {
            'image_path': path,
            'predictions': pred,
            # 'search_results': results
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


def predict(path):
    print('Loading pre-trained inception model...')
    model = Inception(weights='imagenet')
    pred = model.predict(path, top=3)
    # pred = {'Image class': 'confidence score %'}
    pred = dict((p[1].replace('_', ' ').capitalize(), f'{p[2]:.2%}') for p in pred)
    return pred


def search(prediction):
    search = Search()
    results = search.search(prediction)
    return results
