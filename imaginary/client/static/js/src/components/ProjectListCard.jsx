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


const ProjectListCard = (props) => {
  return (
    <article>
      <span className="image">
        <img src={props.image} alt={props.title} />
      </span>
      <header className="major">
        <h3><a href={props.link} className="link">{props.title}</a></h3>
        {props.description}
      </header>
    </article>
  )
};

export default ProjectListCard;
