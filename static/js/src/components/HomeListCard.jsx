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

const HomeListCard = ({image, title, link, description}) =>
  <article>
      <span className="image">
        <img src={image} alt={title}/>
      </span>
    <header className="major">
      <h3><Link to={link} className="link">{title}</Link></h3>
      {description}
    </header>
  </article>;

export default HomeListCard;
