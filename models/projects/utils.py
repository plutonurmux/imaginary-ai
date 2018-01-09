"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 07 January, 2018 @ 7:15 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from werkzeug.utils import secure_filename

from helpers.consts import *


def allowed_file(filename):
    return filename and filename.split('.')[-1] in ALLOWED_EXTENSIONS


def maybe_download_or_upload(file, folder=''):
    status = False
    try:
        if file['type'] == 'upload':
            status = upload_file(file['file'], folder)
        elif file['type'] == 'url':
            status = download_file(file['file'], folder)
    except Exception as e:
        print(f'{e}')
    return status


def download_file(url, download_folder=''):
    print(f'TODO: Download from {url} into {UPLOAD_DIR + "/" + download_folder}!')
    return False


def upload_file(file, upload_folder=''):
    filename = secure_filename(file.filename)
    upload_folder = os.path.join(UPLOAD_DIR, upload_folder)
    if file and allowed_file(filename):
        path = os.path.join(upload_folder, filename)
        if not os.path.isdir(upload_folder):
            os.makedirs(upload_folder)
        file.save(path)
        return path
    raise Exception(f'Image extension can be one of {", ".join(ALLOWED_EXTENSIONS)}')
