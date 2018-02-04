/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 04 February, 2018 @ 10:04 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React, {Component} from 'react';
import {Link} from 'react-router-dom';

import Generic from "../../components/Layouts/Generic";


class ReinforcementLearning extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Generic title="Reinforcement Learning">
        <p><strong>Reinforcement learning (RL)</strong> is an area of <Link
          to="https://en.wikipedia.org/wiki/Machine_learning" target="_blank">machine learning</Link> inspired
          by <Link to="https://en.wikipedia.org/wiki/Behaviorism" target="_blank">behaviourist psychology, </Link>
          concerned with how software agents ought to take actions in an environment so as to maximize some notion
          of cumulative <em>reward.</em> Reinforcement learning requires clever exploration mechanisms. Randomly
          selecting actions, without reference to an estimated probability distribution, shows poor performance. The
          case of (small) finite <Link
            to="https://en.wikipedia.org/wiki/Markov_decision_process" target="_blank">Markov decision
            processes</Link> is relatively well understood. However, due to the lack of algorithms that provably
          scale well with the number of states (or scale to problems with infinite state spaces), simple exploration
          methods are the most practical.</p>
      </Generic>
    );
  }
}

export default ReinforcementLearning;