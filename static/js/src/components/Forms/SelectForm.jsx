/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 04 February, 2018 @ 6:46 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';

const SelectForm = (props) =>
  <div className="select-wrapper">
    <select name="demo-category" id="demo-category">
      {props.hint && <option hidden>- {props.hint} -</option>}
      {props.options.map(option => <option key={option.value} value={option.value}>{option.text}</option>)}
    </select>
  </div>;

export default SelectForm;