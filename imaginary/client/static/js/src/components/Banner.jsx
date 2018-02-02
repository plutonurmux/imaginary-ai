/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 02 February, 2018 @ 12:15 AM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';

const Banner = (props) => {
  return (
    <section id="banner" className="major">
      <div className="inner">
        <header className="major">
          <h1>Hi, my name is Victor</h1>
        </header>
        <div className="content">
          <p>I'm an Artificial Intelligence Engineer and researcher<br/>
            and here's a side piece of my works</p>
          <ul className="actions">
            <li><a href="#one" className="button next scrolly">Get Started</a></li>
          </ul>
        </div>
      </div>
    </section>
  );
};

export default Banner;
