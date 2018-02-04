/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 02 February, 2018 @ 10:37 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React, {Component} from 'react';
import {Link} from 'react-router-dom';

import Generic from "../../components/Layouts/Generic";

class GenerativeModels extends Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Generic title="Generative Models">
        <p>In <Link to="https://en.wikipedia.org/wiki/Probability" target="_blank">probability </Link>
          and <Link to="https://en.wikipedia.org/wiki/Statistics" target="_blank">statistics,</Link> a generative
          model is a model for generating all values for a phenomenon, both those that can be observed in the world
          and "target" variables that can only be computed from those observed. By contrast, discriminative models
          provide a model only for the target variable(s), generating them by analyzing the observed variables. In
          simple terms, <Link to="https://en.wikipedia.org/wiki/Discriminative_model" target="_blank">discriminative
            models</Link> infer outputs based on inputs, while generative models generate both inputs and outputs,
          typically given some <Link to="https://en.wikipedia.org/wiki/Latent_variable" target="_blank">hidden
            parameters.</Link></p>
      </Generic>
    );
  }
}

export default GenerativeModels;
