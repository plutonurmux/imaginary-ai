/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 02 February, 2018 @ 1:22 AM.
 * Copyright © 2018. Victor. All rights reserved.
 */


import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import InnerList from '../../components/InnerList';
import InnerListItem from '../../components/InnerListItem';
import Banner from '../../components/Banner';

class Projects extends Component {

  render() {
    return (
      <div id="main">

        <Banner
          heading="My projects"
          image="/static/images/pic01.jpg"
          description={<p>I started working on some personal A.I. projects<br/>
            mostly after learning some new concepts but also <br/>
            during the process of learning and research.</p>}/>

        {/* Deep learning Projects */}
        <section id="one">
          <InnerListItem
            title="Deep Learning Projects"
            description={<div className="inner">
              <p>Deep Learning is a new area of Machine Learning research, which has been introduced with
                the objective of moving Machine Learning closer to one of its original goals: <strong>
                  ArtificialIntelligence.</strong></p>
              <p>After taking deep learning courses at MIT, Stanford Udacity and Coursera. I started working on projects
                to reinforce some fundamentals and also have fun with the new area of ML research.</p>
              <p>Resources: You'll find interesting datasets on <Link to="http://deeplearning.net/datasets/">
                deeplearning.net</Link> and <Link to="https://www.kaggle.com/datasets">kaggle.com</Link>. Also find some
                useful blog posts on <Link to="https://www.pinchofintelligence.com/">pinchofintelligence.com</Link>,
                <Link to="http://karpathy.github.io/"> Andrej Karpathy</Link>, <Link to="https://iamtrask.github.io/">
                  Andrew Trask</Link> and <Link to="http://colah.github.io/">Chris Olah's</Link> blog posts. To learn
                more about Neural Networks and it's various forms, your best bet is the <Link
                  to="http://www.asimovinstitute.org/neural-network-zoo/">neural network zoo</Link>
              </p>
            </div>}
          />
        </section>

        {/* Deep learning projects */}
        <section id="two" className="spotlights">
          {/*Image Classification */}
          <InnerList
            title="Image Classification" image="/static/images/pic08.jpg"
            link="/projects/image-classification" data_position="center center"
            description={<p>Image classification analyzes the numerical properties of various image features and
              organizes data into categories. Classification algorithms typically employ two phases of processing:
              <em>training</em> and <em>testing.</em> In the initial training phase, characteristic properties of
              typical image features are isolated and, based on these, a unique description of each classification
              category, i.e. <em>training class</em>, is created. In the subsequent testing phase, these feature-space
              partitions are used to classify image features.</p>}/>

          {/*Generative Models */}
          <InnerList
            title="Generative Models" image="/static/images/pic09.jpg"
            link="/projects/generative-models" data_position="top center"
            description={<p>In <Link to="https://en.wikipedia.org/wiki/Probability" target="_blank">probability </Link>
              and <Link to="https://en.wikipedia.org/wiki/Statistics" target="_blank">statistics,</Link> a generative
              model is a model for generating all values for a phenomenon, both those that can be observed in the world
              and "target" variables that can only be computed from those observed. By contrast, discriminative models
              provide a model only for the target variable(s), generating them by analyzing the observed variables. In
              simple terms, <Link to="https://en.wikipedia.org/wiki/Discriminative_model" target="_blank">discriminative
                models</Link> infer outputs based on inputs, while generative models generate both inputs and outputs,
              typically given some <Link to="https://en.wikipedia.org/wiki/Latent_variable" target="_blank">hidden
                parameters.</Link>
            </p>}/>

          {/*Image Search*/}
          <InnerList
            title="Image Search" image="/static/images/pic09.jpg"
            link="/projects/image-search" data_position="25% 25%"
            description={<p>A computer system for browsing, searching and retrieving images from a large
              database of <Link to="https://en.wikipedia.org/wiki/Digital_image" target="_blank">digital images. </Link>
              Most traditional and common methods of image retrieval utilize some method of adding <Link
                to="https://en.wikipedia.org/wiki/Metadata" target="_blank">metadata</Link> such as
              captioning, keywords, or descriptions to the images so that retrieval can be performed over the annotation
              words. Manual image annotation is time-consuming, laborious and expensive; to address this, there has been
              a large amount of research done on <Link to="https://en.wikipedia.org/wiki/Automatic_image_annotation"
                                                       target="_blank">automatic image annotation.</Link> Additionally,
              the increase in social <Link to="https://en.wikipedia.org/wiki/Web_application"
                                           target="_blank">web
                applications</Link> and the <Link to="https://en.wikipedia.org/wiki/Semantic_web" target="_blank">
                semantic web</Link> have inspired the development of several web-based
              image annotation tools.</p>}/>

          {/*A.I. Articles */}
          <InnerList
            title="A.I. Articles" image="/static/images/pic09.jpg"
            link="/projects/ai-articles" data_position="top center"
            description={<p>The <Link to="https://en.wikipedia.org/wiki/Turing_test" target="_blank">Turing test,</Link>
              developed by Alan Turing in 1950, is a test of a machine's ability to <Link
                to="https://en.wikipedia.org/wiki/Artificial_intelligence" target="_blank">exhibit intelligent
                behavior</Link> equivalent to, or indistinguishable from, that of a human. Turing proposed that a human
              evaluator would <Link to="https://en.wikipedia.org/wiki/Natural_language_understanding" target="_blank">judge
                natural language conversations</Link> between a human and a machine designed to generate
              human-like responses. The evaluator would be aware that one of the two partners in conversation is a
              machine, and all participants would be separated from one another. The conversation would be limited to a
              text-only channel such as a computer keyboard and <Link
                to="https://en.wikipedia.org/wiki/Visual_display_unit" target="_blank">screen</Link> so the result would
              not depend on the machine's ability to render words as speech. If the evaluator cannot reliably tell the
              machine from the human, the machine is said to have passed the test.</p>}/>

          {/*Auto Encoding */}
          <InnerList
            title="Auto Encoding" image="/static/images/pic10.jpg"
            link="/projects/auto-encoding" data_position="25% 25%"
            description={<p>Architecturally, the simplest form of an autoencoder is a feedforward,
              non-recurrent neural network very similar to the <Link
                to="https://en.wikipedia.org/wiki/Multilayer_perceptron" target="_blank">multilayer perceptron </Link>
              (MLP) – having an input layer, an output layer and one or more hidden layers connecting them – but with
              the output layer having the same number of nodes as the input layer, and with the purpose of
              reconstructing its own inputs (instead of predicting the target value <kbd>Y</kbd> given inputs
              <kbd>X</kbd>). Therefore, autoencoders are <Link
                to="https://en.wikipedia.org/wiki/Unsupervised_learning" target="_blank">unsupervised learning </Link>
              models.</p>}/>
        </section>

        {/*Reinforcement Learning */}
        <section id="three">
          <InnerListItem
            title="Reinforcement Learning Projects"
            link="/projects/reinforcement-learning"
            icon="next"
            description={<p><strong>Reinforcement learning (RL)</strong> is an area of <Link
              to="https://en.wikipedia.org/wiki/Machine_learning" target="_blank">machine learning</Link> inspired by
              <Link to="https://en.wikipedia.org/wiki/Behaviorism" target="_blank">behaviourist psychology, </Link>
              concerned with how software agents ought to take actions in an environment so as to maximize some notion
              of cumulative <em>reward.</em> Reinforcement learning requires clever exploration mechanisms. Randomly
              selecting actions, without reference to an estimated probability distribution, shows poor performance. The
              case of (small) finite <Link
                to="https://en.wikipedia.org/wiki/Markov_decision_process" target="_blank">Markov decision
                processes</Link> is relatively well understood. However, due to the lack of algorithms that provably
              scale well with the number of states (or scale to problems with infinite state spaces), simple exploration
              methods are the most practical.</p>}/>
        </section>

      </div>
    );
  }
}

export default Projects;
