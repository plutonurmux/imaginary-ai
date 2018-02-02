/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 02 February, 2018 @ 5:45 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';
import {Link} from 'react-router-dom';

import ResearchListItem from './ResearchListItem';

const ResearchList = (props) => {
  return (
    <section>
      <Link to={props.link} className="image">
        <img src={props.image} alt={props.title} data-position="center center"/>
      </Link>
      <div className="content">
        <ResearchListItem {...props} />
      </div>
    </section>
  );
};

export default ResearchList;
