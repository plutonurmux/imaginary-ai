/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 04 February, 2018 @ 10:03 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React, {Component} from 'react';
import {Link} from 'react-router-dom';

import Generic from "../../components/Layouts/Generic";


class AutoEncoding extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Generic title="Auto Encoding">
        <p>Architecturally, the simplest form of an autoencoder is a feedforward,
          non-recurrent neural network very similar to the <Link
            to="https://en.wikipedia.org/wiki/Multilayer_perceptron" target="_blank">multilayer perceptron </Link>
          (MLP) – having an input layer, an output layer and one or more hidden layers connecting them – but with
          the output layer having the same number of nodes as the input layer, and with the purpose of
          reconstructing its own inputs (instead of predicting the target value <kbd>Y</kbd> given inputs
          <kbd>X</kbd>). Therefore, autoencoders are <Link
            to="https://en.wikipedia.org/wiki/Unsupervised_learning" target="_blank">unsupervised learning </Link>
          models.</p>
      </Generic>
    );
  }
}

export default AutoEncoding;