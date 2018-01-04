"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 04 January, 2018 @ 7:28 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import render_template

from views import app


@app.route('/projects/')
def projects():
    return render_template('projects/index.html')


@app.route('/projects/image-classification/')
def image_classification():
    return render_template('projects/image-classification.html')


@app.route('/projects/generative-models/')
def generative_models():
    return render_template('projects/generative-models.html')


@app.route('/projects/ai-articles/')
def ai_articles():
    return render_template('projects/ai-articles.html')


@app.route('/projects/word-embeddings/')
def word_embeddings():
    return render_template('projects/word-embeddings.html')


@app.route('/projects/auto-encoding/')
def auto_encoding():
    return render_template('projects/auto-encoding.html')


@app.route('/projects/reinforcement-learning/')
def reinforcement_learning():
    return render_template('projects/reinforcement-learning.html')
