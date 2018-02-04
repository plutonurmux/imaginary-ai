/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 04 February, 2018 @ 10:00 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import Generic from "../../components/Layouts/Generic";

class AIArticles extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Generic title="A.I. Articles">
        <p>The <Link to="https://en.wikipedia.org/wiki/Turing_test" target="_blank">Turing test,</Link>
          developed by Alan Turing in 1950, is a test of a machine's ability to <Link
            to="https://en.wikipedia.org/wiki/Artificial_intelligence" target="_blank">exhibit intelligent
            behavior</Link> equivalent to, or
          indistinguishable from, that of a human. Turing proposed that a human evaluator
          would <Link
            to="https://en.wikipedia.org/wiki/Natural_language_understanding" target="_blank">judge
            natural language conversations</Link> between a human and a machine designed to generate human-like
          responses. The evaluator would be aware that one of the two partners in conversation is a
          machine, and all participants would be separated from one another. The conversation would be limited to a
          text-only channel such as a computer keyboard and <Link
            to="https://en.wikipedia.org/wiki/Visual_display_unit" target="_blank">screen</Link> so the result would not
          depend on the machine's ability to render words as speech. If the evaluator cannot reliably tell the
          machine from the human, the machine is said to have passed the test.</p>
      </Generic>
    );
  }
}

export default AIArticles;