/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 04 February, 2018 @ 7:47 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';

const ImageGridComponent = ({images}) =>
  <div className="box alt">
    <div className="row 50% uniform">
      {images.map((image, i) =>
        <div className={i % 3 === 0 && i !== 0 ? '4u$' : '4u'} key={i}>
            <span className="image fit">
              <img src={image} alt=""/>
            </span>
        </div>)}
    </div>
  </div>;

export default ImageGridComponent;
