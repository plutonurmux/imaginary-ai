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
// import Home from './containers/Home';
import App from './components/App';

// Projects containers
// import Projects from './containers/projects';
// import ImageClassification from './containers/projects/ImageClassification';
// import GenerativeModels from './containers/projects/GenerativeModels';
// import ImageSearch from './containers/projects/ImageSearch';

// Research containers
// import Research from './containers/research';
// import ALanguageModel from './containers/research/ALanguageModel';
// import ProjectGlass from './containers/research/ProjectGlass';


export default (
  <div>
    <Route exact path="/" component={App}>
      {/* Projects page.*/}
      {/*<Route exact path="/projects" component={Projects}>*/}
        {/*<Route path="/projects/image-classification" component={ImageClassification}/>*/}
        {/*<Route path="/projects/generative-models" component={GenerativeModels}/>*/}
        {/*<Route path="/projects/image-search" component={ImageSearch}/>*/}
      {/*</Route>*/}
      {/* Research page. */}
      {/*<Route path="/research" component={Research}>*/}
        {/*<Route path="/research/a-language-model" component={ALanguageModel}/>*/}
        {/*<Route path="/research/project-glass" component={ProjectGlass}/>*/}
      {/*</Route>*/}
    </Route>
  </div>
);
