/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 02 February, 2018 @ 12:31 AM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';

import HomeListCard from './HomeListCard';

const HomeList = (props) => {

  return (
    <section className='tiles' id='one'>
      {props.lists.map((project) => {
        return <HomeListCard key={project.title} {...project} />
      })}
    </section>
  );
};

export default HomeList;
