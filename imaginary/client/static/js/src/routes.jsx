/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 02 February, 2018 @ 1:19 AM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';
import {Route, IndexRoute} from 'react-router';

// containers
import Home from './containers/Home';
import Projects from './containers/projects';
import Research from './containers/research';


export default (
  <div>
    {/* Home page.*/}
    <Route exact path="/" component={Home}/>

    {/* Projects page.*/}
    <Route path="/projects" component={Projects}/>

    {/* Research page. */}
    <Route path="/research" component={Research}/>

  </div>
);
