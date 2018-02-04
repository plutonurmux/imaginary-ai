/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 04 February, 2018 @ 5:07 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';
import {Link} from 'react-router-dom';

import InnerList from '../../components/InnerList';
import InnerListItem from '../../components/InnerListItem';
import Banner from '../../components/Banner';


const ResearchIndex = ({match}) =>
  <div id="main">
    <Banner
      heading="My Research"
      image="/static/images/pic01.jpg"
      description={<p>Here are some research ideas which has the <br/>
        potential to revolutionize this field.</p>}/>

    {/* Section One */}
    <section id="one">
      {/* Deep learning Research */}
      <InnerListItem
        title="Deep Learning Research"
        description={<p>The greatest impacts of deep learning may well be felt when it is integrated into the whole
          toolbox of other artificial intelligence techniques in ways that haven’t been thought of yet.
          <Link to="https://deepmind.com/" target="_blank">Google’s DeepMind,</Link> for instance, has already been
          accomplishing startling things by combining deep learning with a related technique called reinforcement
          learning. Using the two, it created <Link
            to="https://googleblog.blogspot.com/2016/01/alphago-machine-learning-game-go.html" target="_blank">
            AlphaGo,</Link> the system that, this past March, defeated the champion player of the ancient Chinese
          game of go—widely considered a landmark AI achievement. Unlike IBM’s Deep Blue, which defeated chess
          champion Garry Kasparov in 1997, AlphaGo was not programmed with decision trees, or equations on how to
          evaluate board positions, or with if-then rules. “AlphaGo learned how to play go essentially from
          self-play and from observing big professional games,” says Demis Hassabis, DeepMind’s CEO. (During
          training, AlphaGo played a million go games against itself.)
        </p>}/>
    </section>

    {/* Section Two */}
    <section id="two" className="spotlights">
      {/* A language model. */}
      <InnerList
        title="A Language Model"
        image="/static/images/pic08.jpg" link={`${match.url}/a-language-model`}
        description={<p>A paper was published in June 2016 by Scott Reed et al. that <Link
          to="https://arxiv.org/pdf/1605.05396.pdf" target="_blank">generates realistic images from just
          text descriptions,</Link> they are called <Link to="https://arxiv.org/abs/1406.2661" target="_blank">Generative
          Adversarial Networks (or GANs).</Link> The important thing to note about
          this model is that it's an unsupervised learning algorithm. i.e. it trains with no label what so ever...
          You just give it (the GAN) a phrase or caption, and then it outputs image which matches the caption you
          gave it.</p>}/>
      {/* Project Glass */}
      <InnerList
        title="Project Glass"
        image="/static/images/pic09.jpg" link={`${match.url}/project-glass`}
        description={<p>Everybody should be given equal rights. Everyone. Including the disabled. There are set of
          human beings who do not fit into this world because of their disabilities. I believe everyone should have
          equal chances; the way one uses his/her chance is up to him/her. In order to make this happen, the blind
          needs to see, the deaf needs to hear, the crippled need to walk again.</p>}/>
    </section>

    {/* Section Three */}
    <section id="three">
      {/* Reinforcement learning Research */}
      <InnerListItem
        title="Reinforcement Learning Research" icon="next"
        description={<p>A game might seem like an artificial setting. But Hassabis thinks the same techniques can be
          applied to real-world problems. In July, in fact, Google reported that, by using approaches similar to
          those used by AlphaGo, DeepMind was able to increase the energy efficiency of Google’s data centers by
          15%. “In the data centers there are maybe 120 different variables,” says Hassabis. “You can change the
          fans, open the windows, alter the computer systems, where the power goes. You’ve got data from the
          sensors, the temperature gauges, and all that. It’s like the go board. Through trial and error, you learn
          what the right moves are.</p>}/>
    </section>
  </div>;

export default ResearchIndex;