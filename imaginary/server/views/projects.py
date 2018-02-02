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
def image_classification():
    return render_template('projects/image-classification.html')


@app.route('/projects/generative-models/')
def generative_models():
    return render_template('projects/generative-models.html')


@app.route('/projects/image-search/')
def image_search():
    return render_template('projects/image-search.html')


@app.route('/projects/ai-articles/')
def ai_articles():
    return render_template('projects/ai-articles.html')


@app.route('/projects/auto-encoding/')
def auto_encoding():
    return render_template('projects/auto-encoding.html')


@app.route('/projects/reinforcement-learning/')
def reinforcement_learning():
    return render_template('projects/reinforcement-learning.html')
