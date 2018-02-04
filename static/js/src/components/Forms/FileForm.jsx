/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 04 February, 2018 @ 6:51 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';

const FileForm = (props) =>
  <div className="input-group mb-3">
    <div className="input-group-prepend">
      <button className={`button special fit${props.icon ? ' icon ' + props.icon : ''}`}
              type="submit" name={props.name}>{props.value}</button>
    </div>
    <div className="custom-file">
      <input type="file" className="custom-file-input" name={props.inputName} id={`${props.inputName}-file`}/>
      <label className="custom-file-label" htmlFor={`${props.inputName}-file`}>{props.hint || ''}</label>
    </div>
  </div>;

export default FileForm;
