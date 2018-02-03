/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 02 February, 2018 @ 5:44 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';
import {Link} from 'react-router-dom';

const InnerListItem = (props) => {
  return (
    <div className="inner">
      <header className="major">
        <h3>{props.title}</h3>
      </header>
      {props.description}
      {props.link ? <ul className="actions">
        <li>
          <Link to={props.link} className={`button ${props.icon || ''}`}>Learn more</Link>
        </li>
      </ul> : null}
    </div>
  );
};

export default InnerListItem;
