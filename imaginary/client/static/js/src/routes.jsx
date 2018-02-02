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
import Projects from './containers/Projects';


export default (
  <div>
    <Route exact path="/" component={Home}/>
    <Route path="/projects" component={Projects}>
      <Route path="a-language-model" component={Projects}/>
    </Route>

  </div>
);
