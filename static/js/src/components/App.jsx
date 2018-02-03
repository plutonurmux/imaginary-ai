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
import Header from './Layouts/Header';
import Nav from './Layouts/Nav';
import Footer from './Layouts/Footer';

const App = (props) => {
  return (
    <div>
      <Header {...props} />
      <Nav/>
      <div id="main">{props.children}</div>
      <Footer/>
    </div>
  );
};

export default App;
