"""
  @author Victor I. Afolabi
  
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 01 February, 2018 @ 11:43 PM.
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import render_template

from imaginary.server import app, back


@app.route('/projects/')
@back.anchor
def projects():
    return render_template('projects/index.html')


@app.route('/projects/image-classification/')
@back.anchor
def image_classification():
    """
    Project's Image classification page.

    :return: HTML template.
    """
    return render_template('projects/image-classification.html')


@app.route('/projects/generative-models/')
@back.anchor
def generative_models():
    """
    Project's Generative models page.

    :return: HTML template.
    """
    return render_template('projects/generative-models.html')


@app.route('/projects/image-search/')
@back.anchor
def image_search():
    """
    Project's Image search page.

    :return: HTML template.
    """
    return render_template('projects/image-search.html')


@app.route('/projects/ai-articles/')
@back.anchor
def ai_articles():
    """
    Project's A.I. Articles page.

    :return: HTML template.
    """
    return render_template('projects/ai-articles.html')


@app.route('/projects/auto-encoding/')
@back.anchor
def auto_encoding():
    """
    Project's Auto encoding page.

    :return: HTML template.
    """
    return render_template('projects/auto-encoding.html')


@app.route('/projects/reinforcement-learning/')
@back.anchor
def reinforcement_learning():
    """
    Project's Reinforcement learning page.

    :return: HTML template.
    """
    return render_template('projects/reinforcement-learning.html')
