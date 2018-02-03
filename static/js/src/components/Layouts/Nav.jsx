/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 03 February, 2018 @ 9:51 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';
import {Link} from 'react-router-dom';

const Nav = () =>
  <nav id="menu">
    <ul className="links">
      <li><Link to="/">Home</Link></li>
      <li><Link to="/projects">Projects</Link></li>
      <li><Link to="/research">Research</Link></li>
    </ul>

    <ul className="actions vertical">
      <li><Link to="#" className="button special fit">Get Started</Link></li>
      <li><Link to="#" className="button fit">Log In</Link></li>
    </ul>
  </nav>;


export default Nav;
