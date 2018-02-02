/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 02 February, 2018 @ 12:17 AM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import Banner from '../components/Banner';
import HomeList from '../components/HomeList';
import InnerListItem from '../components/InnerListItem'

class Home extends Component {

  constructor(props) {
    super(props);
    this.state = {
      project_list: [
        {
          title: 'Image Classification',
          link: 'projects/image-classification/',
          image: '/static/images/pic01.jpg',
          'description': <p>Image classification with <span>Convolutional Neural Networks</span></p>
        },
        {
          title: 'Generative Models',
          link: 'projects/generative-models/',
          image: '/static/images/pic02.jpg',
          'description': <p>Generate photo realistic images with <span>Generative Adversarial Networks</span></p>
        },
        {
          title: 'Image Search',
          link: 'projects/image-search/',
          image: '/static/images/pic03.jpg',
          'description': <p>Let's see how we can search the web by image after we know what's in it. Thanks to <span>Convolutional Neural Network</span>
          </p>
        },
        {
          title: 'A.I. Article',
          link: 'projects/ai-articles/',
          image: '/static/images/pic04.jpg',
          description: <p>Articles written by A.I. with <span>Recurrent Neural Networks</span></p>
        },
        {
          title: 'Auto Encoding',
          link: 'projects/auto-encoding/',
          image: '/static/images/pic05.jpg',
          description: <p>Create variations of a single image with <span>Variational Auto Encoders</span></p>
        },
        {
          title: 'Reinforcement Learning',
          link: 'projects/reinforcement-learning/',
          image: '/static/images/pic06.jpg',
          description: <p>Checkout this A.I. agent that learns through the process of <span>Trial &amp; Error</span></p>
        },
      ]
    };

  }

  render() {
    return (
      <div id="main">
        <Banner
          link="#one" link_text="Get Started" style="next scrolly"
          heading="Hi, my name is Victor"
          description={<p>I'm an Artificial Intelligence Engineer and researcher
            <br/> and here's a side piece of my works</p>}/>
        <div id="main">
          <HomeList lists={this.state.project_list}/>
          <section id="two">
            <InnerListItem
              title="A Language Model"
              link="/research/a-language-model"
              icon="next"
              description={<p>I discovered something which might lead to a major breakthrough in the field of A.I. and
                NLP <em>(Natural Language Processing)...</em> I did some math to see how it improves existing models
                and it was pretty damn good. It's on the topic of AI developing some abstract representation of
                concepts. I'm sorry if this doesn't makes sense but it's really a cool concepts which is what humans do
                unconsciously. I've always wanted to build and do sth amazing and meaningful for the whole world...</p>}
            />
          </section>
        </div>
      </div>
    );
  }
}

export default Home;
