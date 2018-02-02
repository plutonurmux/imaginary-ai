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
import InnerList from '../components/InnerList';
import InnerListItem from '../components/InnerListItem';


class Research extends Component {
  render() {
    return (
      <div id="main">
        {/* Section One */}
        <section id="one">
          <InnerListItem
            title="Deep Learning Research"
            actions={false} link="#"
            description={<p>Nullam et orci eu lorem consequat tincidunt vivamus et sagittis magna sed nunc rhoncus
              condimentum sem. In efficitur ligula tate urna. Maecenas massa sed magna lacinia magna pellentesque
              lorem ipsum dolor. Nullam et orci eu lorem consequat tincidunt. Vivamus et sagittis tempus.</p>}
          />
        </section>

        {/* Section Two */}
        <section id="two" className="spotlights">
          {/* A language model. */}
          <InnerList
            title="A Language Model"
            image="/static/images/pic08.jpg"
            link="/research/a-language-model"
            description={<p>Nullam et orci eu lorem consequat tincidunt vivamus et sagittis magna sed nunc rhoncus
              condimentum sem. In efficitur ligula tate urna. Maecenas massa sed magna lacinia magna pellentesque
              lorem ipsum dolor. Nullam et orci eu lorem consequat tincidunt. Vivamus et sagittis tempus.</p>}
          />
          {/* Project Glass */}
          <InnerList
            title="Project Glass"
            image="/static/images/pic08.jpg"
            link="/research/project-glass"
            description={<p>Nullam et orci eu lorem consequat tincidunt vivamus et sagittis magna sed nunc rhoncus
              condimentum sem. In efficitur ligula tate urna. Maecenas massa sed magna lacinia magna pellentesque
              lorem ipsum dolor. Nullam et orci eu lorem consequat tincidunt. Vivamus et sagittis tempus.</p>}
          />
        </section>

        {/* Section Three */}
        <section id="three">
          {/* Reinforcement learning Research */}
          <InnerListItem
            title="Reinforcement Learning Research"
            icon="next" actions={false} link="#"
            description={<p>Nullam et orci eu lorem consequat tincidunt vivamus et sagittis libero. Mauris aliquet magna
              magna sed nunc rhoncus pharetra. Pellentesque condimentum sem. In efficitur ligula tate urna. Maecenas
              laoreet massa vel lacinia pellentesque lorem ipsum dolor. Nullam et orci eu lorem consequat
              tincidunt.</p>}
          />
        </section>
      </div>
    );
  }
}

export default Research;
