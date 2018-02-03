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
import {Link} from 'react-router-dom';

const Banner = (props) => {
  return (
    <section id="banner" className="major">
      <div className="inner">
        <header className="major">
          <h1>{props.heading}</h1>
        </header>
        <div className="content">
          {props.description}
          <ul className="actions">
            <li>
              <Link to={props.link} className={`button ${props.style || ''}`}>
                {props.link_text}
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </section>
  );
};

export default Banner;
