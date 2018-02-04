/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 02 February, 2018 @ 1:22 AM.
 * Copyright © 2018. Victor. All rights reserved.
 */


import React, {Component} from 'react';
import {Route} from 'react-router-dom';

import ImageClassification from './ImageClassification';
import GenerativeModels from './GenerativeModels';
import ImageSearch from './ImageSearch';
import ProjectsIndex from "./ProjectsIndex";

const Projects = (props) =>
  <div id="main">
    <Route exact path={props.match.url}
           render={() => <ProjectsIndex {...props}/>}/>
    {/* Projects */}
    <Route path={`${props.match.path}/image-classification`}
           render={({match}) => <ImageClassification {...props} />}/>
    <Route path={`${props.match.path}/generative-models`}
           render={({match}) => <GenerativeModels {...props} />}/>
    <Route path={`${props.match.path}/image-search`}
           render={({match}) => <ImageSearch {...props}/>}/>
  </div>;

export default Projects;
