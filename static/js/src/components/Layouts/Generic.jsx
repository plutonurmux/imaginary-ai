/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 04 February, 2018 @ 4:41 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';

const Generic = (props) =>
  <section id="one">
    <div className="inner">
      <header className="major">
        <h1>{props.title}</h1>
      </header>
      <span className="image main">
        <img src={`${props.image || '/static/images/pic11.jpg'}`} alt={props.title}/>
       </span>
      {props.children}
    </div>
  </section>;

export default Generic;
