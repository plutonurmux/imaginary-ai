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

import {FOOTER_LINKS} from "../../constants/links";

const Footer = () =>
  <footer id="footer">
    <div className="inner">
      <ul className="icons">
        {FOOTER_LINKS.map(item =>
          <li key={item.label}>
            <Link to={item.link} className={`icon alt ${item.icon}`}>
              <span className="label">{item.label}</span>
            </Link>
          </li>)}
      </ul>
      <ul className="copyright">
        <li>&copy; 2018. Imaginary A.I.</li>
        <li>Design:
          <a href="https://github.com/victor-iyiola">Victor I. Afolabi</a>
        </li>
      </ul>
    </div>
  </footer>;

export default Footer;
