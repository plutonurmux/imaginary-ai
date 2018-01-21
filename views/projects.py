"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com

  Created on 04 January, 2018 @ 7:28 PM.

  Copyright © 2018. Victor. All rights reserved.
"""

from flask import render_template, request
# helper module for image classification
import models.projects.image_classification as img_class
# helper module for image search
import models.projects.image_search as img_search
from views import app, back


@app.route('/projects/')
@back.anchor
def projects():
    """Projects page.

    Decorators:
        back
        app

    Returns:
        [template] -- [renders page template]
    """

    return render_template('projects/index.html')


@app.route('/projects/image-classification/', methods=['GET', 'POST'])
@back.anchor
def image_classification():
    """Image classification page.

    Decorators:
        back
        app

    Returns:
        [type] -- [description]
    """
    return render_template('projects/image-classification.html')


@app.route('/projects/generative-models/')
@back.anchor
def generative_models():
    """Generative models page.

    Decorators:
        back
        app

    Returns:
        [template] -- [renders page template]
    """

    return render_template('projects/generative-models.html')


@app.route('/projects/image-search/', methods=['GET', 'POST'])
@back.anchor
def image_search():
    """Image search page.

    Decorators:
        back
        app

    Returns:
        [template] -- [renders page template]
    """

    if request.method == 'POST':
        try:
            data = img_search.process(request)
            return render_template('projects/image-search.html', data=data)
        except Exception as e:
            print(f'ERROR: {e}')
            return render_template('projects/image-search.html', error=e)
    # !- request.method == 'GET'
    return render_template('projects/image-search.html')


@app.route('/projects/ai-articles/')
@back.anchor
def ai_articles():
    """A.I. Articles page.

    Decorators:
        back
        app

    Returns:
        [template] -- [renders page template]
    """

    return render_template('projects/ai-articles.html')


@app.route('/projects/auto-encoding/')
@back.anchor
def auto_encoding():
    """Auto encoding page.

    Decorators:
        back
        app

    Returns:
        [template] -- [renders page template]
    """

    return render_template('projects/auto-encoding.html')


@app.route('/projects/reinforcement-learning/')
@back.anchor
def reinforcement_learning():
    """Reinforcement learning page.

    Decorators:
        back
        app

    Returns:
        [template] -- [renders page template]
    """

    return render_template('projects/reinforcement-learning.html')
