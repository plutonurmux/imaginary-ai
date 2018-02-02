/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 02 February, 2018 @ 12:24 AM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';
import {Link} from 'react-router-dom';

const HomeListCard = (props) => {
  return (
    <article>
      <span className="image">
        <img src={props.image} alt={props.title} />
      </span>
      <header className="major">
        <h3><Link to={props.link} className="link">{props.title}</Link></h3>
        {props.description}
      </header>
    </article>
  )
};

export default HomeListCard;
