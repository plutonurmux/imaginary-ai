"""
  @author Victor I. Afolabi

  A.I. Engineer & Software developer
  javafolabi@gmail.com

  Created on 01 February, 2018 @ 2:45 PM.
  Copyright (c) 2018. Victor. All rights reserved.
"""

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--debug', default=True,
                    help='Run the web server in debug mode.')
args = parser.parse_args()


if __name__ == '__main__':
    from application import app
    app.run(debug=args.debug)
