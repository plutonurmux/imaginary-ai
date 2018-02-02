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


class Projects extends Component {

  render() {
    return (
      <div id="main">
        {/* Deep learning Projects */}
        <section id="one">
          <InnerListItem
            title="Deep Learning Projects"
            link="#" actions={false}
            description={<div className="inner">
              <p>Deep Learning is a new area of Machine Learning research, which has been introduced with
                the objective of moving Machine Learning closer to one of its original goals:
                <strong> ArtificialIntelligence.</strong></p>
              <p>After taking deep learning courses at MIT, Stanford Udacity and Coursera. I started working on projects
                to reinforce some fundamentals and also have fun with the new area of ML research.</p>
              <p>Resources: You'll find interesting datasets on
                <Link to="http://deeplearning.net/datasets/"> deeplearning.net</Link> and
                <Link to="https://www.kaggle.com/datasets"> kaggle.com</Link>. Also find some useful blog posts on
                <Link to="https://www.pinchofintelligence.com/"> pinchofintelligence.com</Link>,
                <Link to="http://karpathy.github.io/"> Andrej Karpathy</Link>,
                <Link to="https://iamtrask.github.io/"> Andrew Trask</Link> and
                <Link to="http://colah.github.io/"> Chris Olah's</Link> blog posts. To learn more about Neural Networks
                and it's various forms, your best bet is the
                <Link to="http://www.asimovinstitute.org/neural-network-zoo/"> neural network zoo</Link>
              </p>
            </div>}
          />
        </section>

        {/* Deep learning projects */}
        <section id="two" className="spotlights">
          {/*Image Classification */}
          <InnerList
            title="Image Classification" image="/static/images/pic08.jpg"
            link="/projects/image-classification/" data_position="center center"
            description={<p>Nullam et orci eu lorem consequat tincidunt vivamus et sagittis magna sed nunc rhoncus
              condimentumsem. In efficitur ligula tate urna. Maecenas massa sed magna lacinia magna pellentesque lorem
              ipsum dolor. Nullam et orci eu lorem consequat tincidunt. Vivamus et sagittis tempus.</p>}/>

          {/*Generative Models */}
          <InnerList
            title="Generative Models" image="/static/images/pic09.jpg"
            link="/projects/generative-models" data_position="top center"
            description={<p>Nullam et orci eu lorem consequat tincidunt vivamus et sagittis magna sed nunc rhoncus
              condimentumsem. In efficitur ligula tate urna. Maecenas massa sed magna lacinia magna pellentesque lorem
              ipsum dolor. Nullam et orci eu lorem consequat tincidunt. Vivamus et sagittis tempus.</p>}/>

          {/*Image Search*/}
          <InnerList
            title="Image Search" image="/static/images/pic09.jpg"
            link="/projects/image-search" data_position="25% 25%"
            description={<p>Nullam et orci eu lorem consequat tincidunt vivamus et sagittis magna sed nunc rhoncus
              condimentumsem. In efficitur ligula tate urna. Maecenas massa sed magna lacinia magna pellentesque lorem
              ipsum dolor. Nullam et orci eu lorem consequat tincidunt. Vivamus et sagittis tempus.</p>}/>

          {/*A.I. Articles */}
          <InnerList
            title="A.I. Articles" image="/static/images/pic09.jpg"
            link="/projects/ai-articles" data_position="top center"
            description={<p>Nullam et orci eu lorem consequat tincidunt vivamus et sagittis magna sed nunc rhoncus
              condimentumsem. In efficitur ligula tate urna. Maecenas massa sed magna lacinia magna pellentesque lorem
              ipsum dolor. Nullam et orci eu lorem consequat tincidunt. Vivamus et sagittis tempus.</p>}/>

          {/*Auto Encoding */}
          <InnerList
            title="Auto Encoding" image="/static/images/pic10.jpg"
            link="/projects/auto-encoding" data_position="25% 25%"
            description={<p>Nullam et orci eu lorem consequat tincidunt vivamus et sagittis magna sed nunc rhoncus
              condimentumsem. In efficitur ligula tate urna. Maecenas massa sed magna lacinia magna pellentesque lorem
              ipsum dolor. Nullam et orci eu lorem consequat tincidunt. Vivamus et sagittis tempus.</p>}/>
        </section>

        {/*Reinforcement Learning */}
        <section id="three">
          <InnerListItem
            title="Reinforcement Learning Projects"
            link="/projects/reinforcement-learning"
            icon="next"
            description={<p>Nullam et orci eu lorem consequat tincidunt vivamus et sagittis magna sed nunc rhoncus
              condimentumsem. In efficitur ligula tate urna. Maecenas massa sed magna lacinia magna pellentesque lorem
              ipsum dolor. Nullam et orci eu lorem consequat tincidunt. Vivamus et sagittis tempus.</p>}/>
        </section>

      </div>
    );
  }
}

export default Projects;
