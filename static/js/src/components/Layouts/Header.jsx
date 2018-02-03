/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 03 February, 2018 @ 9:49 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';
import {Link} from 'react-router-dom';

const Header = (props) =>
  <header id="header" className={`alt ${props.style || ''}`}>
    <Link to="/" class="logo">
      <strong>Imaginary A.I.</strong>
      <span>by Victor</span>
    </Link>
    <nav>
      <Link to="#menu">Menu</Link>
    </nav>
  </header>;

export default Header;
