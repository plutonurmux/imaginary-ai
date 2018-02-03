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
    <section id="banner" className={`${props.image ? 'style2' : 'major'}`}>
      <div className="inner">
        {/* Background image. */}
        {props.image ?
          <span className="image">
            <img src={props.image} alt={props.alt || ''}/>
          </span> : null}
        <header className="major">
          <h1>{props.heading}</h1>
        </header>
        <div className="content">
          {props.description}
          {/* Button */}
          {props.link ?
            <ul className="actions">
              <li>
                <Link to={props.link} className={`button ${props.style || ''}`}>
                  {props.link_text}
                </Link>
              </li>
            </ul> : null}
        </div>
      </div>
    </section>
  );
};

export default Banner;
