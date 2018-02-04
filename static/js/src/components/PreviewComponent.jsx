/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 04 February, 2018 @ 6:26 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';

const PreviewComponent = ({title, image}) =>
  <div className="image fit" id="preview">
    <h3>{title}</h3>
    <img src={image} alt={title}/>
  </div>;

export default PreviewComponent;