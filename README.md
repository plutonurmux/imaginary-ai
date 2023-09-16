# Imaginary A.I.

A portfolio-ish platform that helps visualize some of my interesting Artificial Intelligence projects and researches.

Deep Learning is a new area of Machine Learning research, which has been introduced with the objective of moving Machine Learning closer to one of its original goals: **Artificial Intelligence.**

After taking deep learning courses at MIT, Stanford Udacity and Coursera. I started working on projects to reinforce some fundamentals and also have fun with the new area of ML research.

Resources: You'll find interesting datasets on [deeplearning.net](http://deeplearning.net/datasets/) and [kaggle.com](https://www.kaggle.com/datasets). Also find some useful blog posts on [pinchofintelligence.com](https://www.pinchofintelligence.com/), [Andrej Karpathy](http://karpathy.github.io/), [Andrew Trask](https://iamtrask.github.io/) and [Chris Olah's](http://colah.github.io/) blog posts. To learn more about Neural Networks and it's various forms, your best bet is the [neural network zoo](http://www.asimovinstitute.org/neural-network-zoo/)

## Projects

- Image Classification
- Generative Models
- Image Search
- A.I. Articles
- Auto-encoding
- Reinforcement Learning

## Research

- A language model
- Project Glass
- Exploration Exploitation Explanation

## Dependencies

- Language
  - [Python ^3.6.4](http://python.org/)
  - [Node](https://nodejs.org) 
  - [NPM](https://www.npmjs.com)
 
- Other Dependencies
  - [Flask](http://flask.pocoo.org/) – ```pip install flask```
  - [Keras](http://keras.io/) – ```pip install keras```
  - [Numpy](http://www.numpy.org/) – ```pip install numpy```
  - [Pandas](https://pandas.pydata.org/) – ```pip install pandas```
  - [Cython](http://cython.org/) – ```pip install cython```

## Setup

Clone this repo 
```commandline
git clone https://github.com/victor-iyiola/imaginary-ai.git
```

Or download the project [here](https://github.com/victor-iyiola/imaginary-ai/archive/master.zip)

Then change your working directory as show below
```commandline
cd imaginary-ai
```

Install python dependencies
```commandline
pip install --upgrade pip
pip install --upgrade -r requirements.txt
```

Install npm dependencies
```commandline
cd static
npm install
```

After installing the dependencies. You can now start webpack (to compile all client files into a single javascript file. `bundle.js`)

For development
```commandline
npm run watch
```

For Production
```commandline
npm run build
```

Excellent. Now it's time to start the Python (flask) web server.
```
cd <imaginary-ai>
python run.py --debug=True
```
## Contributions

This project is opened under [MIT 2.0 license](https://github.com/victor-iyiola/imaginary-ai/blob/master/LICENSE).
