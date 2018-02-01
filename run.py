"""
  @author Victor I. Afolabi
  
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 01 February, 2018 @ 2:45 PM.
  Copyright © 2018. Victor. All rights reserved.
"""

import argparse
import subprocess
from imaginary.settings import STATIC_FOLDER

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--debug', default=True, help='Run the web server in debug mode.')

args = parser.parse_args()


def run_webpack():
    subprocess.call('cd {} && npm run watch'.format(STATIC_FOLDER.replace(' ', '\ ')), shell=True)


if __name__ == '__main__':
    from imaginary.server import app

    # import multiprocessing
    # process = multiprocessing.Process(target=run_webpack)
    # process.start()
    # process.join()

    app.run(debug=args.debug)
