/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 03 February, 2018 @ 11:49 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';


/*
 * +-------------------------------------------------------------------------------------+
 * | +---------------------------------------------------------------------------------+ |
 * | | List of projects to be displayed in the Home page.
 * | +---------------------------------------------------------------------------------+ |
 * +-------------------------------------------------------------------------------------+
 */
export const PROJECT_LIST = [
  {
    title: 'Image Classification',
    link: '/projects/image-classification',
    image: '/static/images/pic01.jpg',
    description: <p>Image classification with <span>Convolutional Neural Networks</span></p>
  },
  {
    title: 'Generative Models',
    link: '/projects/generative-models/',
    image: '/static/images/pic02.jpg',
    description: <p>Generate photo realistic images with <span>Generative Adversarial Networks</span></p>
  },
  {
    title: 'Image Search',
    link: '/projects/image-search/',
    image: '/static/images/pic03.jpg',
    description: <p>Let's see how we can search the web by image after we know what's in it. Thanks to
      <span>Convolutional Neural Network</span></p>
  },
  {
    title: 'A.I. Article',
    link: '/projects/ai-articles/',
    image: '/static/images/pic04.jpg',
    description: <p>Articles written by A.I. with <span>Recurrent Neural Networks</span></p>
  },
  {
    title: 'Auto Encoding',
    link: '/projects/auto-encoding/',
    image: '/static/images/pic05.jpg',
    description: <p>Create variations of a single image with <span>Variational Auto Encoders</span></p>
  },
  {
    title: 'Reinforcement Learning',
    link: '/projects/reinforcement-learning/',
    image: '/static/images/pic06.jpg',
    description: <p>Checkout this A.I. agent that learns through the process of <span>Trial &amp; Error</span></p>
  },
];


/*
 * +-------------------------------------------------------------------------------------+
 * | +---------------------------------------------------------------------------------+ |
 * | | Footer icons
 * | +---------------------------------------------------------------------------------+ |
 * +-------------------------------------------------------------------------------------+
 */
export const FOOTER_LINKS = [
  {
    label: 'Twitter',
    icon: 'fa-twitter',
    link: 'https://twitter.com/victor_iyi'
  },
  {
    label: 'Facebook',
    icon: 'fa-facebook',
    link: 'https://www.facebook.com/victor.i.afolabi'
  },
  {
    label: 'Instagram',
    icon: 'fa-instagram',
    link: 'https://www.instagram.com/victor_iyiola/'
  },
  {
    label: 'Medium',
    icon: 'fa-medium',
    link: 'https://medium.com/@javafolabi/'
  },
  {
    label: 'GitHub',
    icon: 'fa-github',
    link: 'https://github.com/victor-iyiola'
  },
  {
    label: 'LinkedIn',
    icon: 'fa-linkedin',
    link: 'https://www.linkedin.com/in/victor-i-afolabi-84629b87/'
  },
];
