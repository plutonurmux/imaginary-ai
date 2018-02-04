/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 04 February, 2018 @ 10:35 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';
import {Link} from 'react-router-dom';

import Generic from "./Layouts/Generic";
import {HTTP_STATUS_CODES} from "../constants/status";

/**
 * Error page component.
 *
 * @param props {object} - code, type, message.
 * Example:
 * code = 404,
 * type = Not Found,
 * message = The page your are visiting does not exist. Check the URL and try again.
 * @constructor
 */
const ErrorPage = (props) =>
  <Generic title={`ERROR ${props.code}: ${HTTP_STATUS_CODES[props.code]}`}>
    <p>{props.message}</p>
    <ul className="actions">
      <li><Link to="" class="button icon fa-arrow-left">Take me back</Link></li>
    </ul>
  </Generic>;

export default ErrorPage;