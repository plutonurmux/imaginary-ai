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
import ProjectList from '../components/ProjectList';

class Home extends Component {
  render() {
    return (
      <div>
        <Banner/>
        <div id="main">
          <ProjectList/>
          <section id="two">
            <div className="inner">
              <header className="major">
                <h2>A Language Model</h2>
              </header>
              <p>
                I discovered something which might lead to a major breakthrough in the field of A.I. and NLP <em>(Natural
                Language Processing)...</em> I did some math to see how it improves existing models and it was pretty
                damn good. It's on the topic of AI developing some abstract representation of concepts. I'm sorry if
                this doesn't makes sense but it's really a cool concepts which is what humans do unconsciously. I've
                always wanted to build and do sth amazing and meaningful for the whole world...
              </p>
              <ul className="actions">
                <li><Link to="/research/a-language-model" className="button next">Learn More</Link></li>
              </ul>
            </div>
          </section>
        </div>
      </div>
    );
  }
}

export default Home;
