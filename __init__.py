"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 04 January, 2018 @ 4:59 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from views import *

if __name__ == '__main__':
    app.run(debug=True)


"""
views.py
from flask import Flask, render_template

import helpers.config as cfg

app = Flask(cfg.APP_NAME)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/landing/')
def landing():
    return render_template('landing.html')


@app.route('/elements/')
def elements():
    return render_template('elements.html')


@app.route('/generic/')
def generic():
    return render_template('generic.html')


################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Projects
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
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


################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Research
# |     /research/*
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
@app.route('/research/a-language-model/')
def research():
    return render_template('research/a-language-model.html')
"""