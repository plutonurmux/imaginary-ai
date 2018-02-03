/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 02 February, 2018 @ 2:52 AM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import InnerList from '../../components/InnerList';
import InnerListItem from '../../components/InnerListItem';


class Research extends Component {
  render() {
    return (
      <div id="main">
        {/* Section One */}
        <section id="one">
          {/* Deep learning Research */}
          <InnerListItem
            title="Deep Learning Research"
            actions={false} link="#"
            description={<p>Nullam et orci eu lorem consequat tincidunt vivamus et sagittis magna sed nunc rhoncus
              condimentumsem. In efficitur ligula tate urna. Maecenas massa sed magna lacinia magna pellentesque lorem
              ipsum dolor. Nullam et orci eu lorem consequat tincidunt. Vivamus et sagittis tempus.</p>}/>
        </section>

        {/* Section Two */}
        <section id="two" className="spotlights">
          {/* A language model. */}
          <InnerList
            title="A Language Model"
            image="/static/images/pic08.jpg" link="/research/a-language-model"
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
            image="/static/images/pic09.jpg" link="/research/project-glass"
            description={<p>Everybody should be given equal rights. Everyone. Including the disabled. There are set of
              human beings who do not fit into this world because of their disabilities. I believe everyone should have
              equal chances; the way one uses his/her chance is up to him/her. In order to make this happen, the blind
              needs to see, the deaf needs to hear, the crippled need to walk again.</p>}/>
        </section>

        {/* Section Three */}
        <section id="three">
          {/* Reinforcement learning Research */}
          <InnerListItem
            title="Reinforcement Learning Research"
            icon="next" actions={false} link="#"
            description={<p>Nullam et orci eu lorem consequat tincidunt vivamus et sagittis magna sed nunc rhoncus
              condimentumsem. In efficitur ligula tate urna. Maecenas massa sed magna lacinia magna pellentesque lorem
              ipsum dolor. Nullam et orci eu lorem consequat tincidunt. Vivamus et sagittis tempus.</p>}/>
        </section>
      </div>
    );
  }
}

export default Research;
