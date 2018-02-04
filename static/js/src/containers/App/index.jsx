/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 01 February, 2018 @ 2:20 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React, {Component} from 'react';
import {Switch, Route} from 'react-router-dom';

import Header from '../../components/Layouts/Header';
import Nav from '../../components/Layouts/Nav';
import Footer from '../../components/Layouts/Footer';
import Contact from '../../components/Contact/index';

import Home from '../Home/index';
import Projects from '../Projects';
import Research from '../Research';

class App extends Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div id="main">
        <Header style="style2"/>
        <Nav/>
        <div id="main">
          <Switch>
            <Route exact path="/" component={Home}/>
            <Route path="/projects" component={Projects}/>
            <Route path="/research" component={Research}/>
          </Switch>
        </div>
        <Contact/>
        <Footer/>
      </div>
    );
  }
}

export default App;
