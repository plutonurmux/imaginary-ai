/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 02 February, 2018 @ 2:52 AM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React, {Component} from 'react';
import {Route, Switch} from 'react-router-dom';

import ResearchIndex from './ResearchIndex';
import ALanguageModel from './ALanguageModel';
import ProjectGlass from './ProjectGlass';


const Research = (props) =>
  <Switch>
    <Route exact path={props.match.url}
           render={(props) => <ResearchIndex {...props}/>}/>
    {/* Researches */}
    <Route path={`${props.match.path}/a-language-model`}
           render={(props) => <ALanguageModel {...props} />}/>
    <Route path={`${props.match.path}/project-glass`}
           render={(props) => <ProjectGlass {...props} />}/>
  </Switch>;

export default Research;
