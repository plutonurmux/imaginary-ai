/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 04 February, 2018 @ 2:51 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';
import {Link} from 'react-router-dom';

const ContactDetails = () =>
  <section className="split">
    <section>
      <div className="contact-method">
        <span className="icon alt fa-envelope"/>
        <h3>Email</h3>
        <Link to="https://mailto:javafolabi@gmail.com" target="_blank">
          javafolabi@gmail.com
        </Link>
      </div>
    </section>
    <section>
      <div className="contact-method">
        <span className="icon alt fa-phone"/>
        <h3>Phone</h3>
        <span>(+234) 814-120-5245</span>
      </div>
    </section>
    <section>
      <div className="contact-method">
        <span className="icon alt fa-home"/>
        <h3>Address</h3>
        <span>
            #25, Segun Akinlade Street,
            <br/> Off Akure High School Road,
            <br/> Akure, Ondo State,
            <br/> Nigeria.
          </span>
      </div>
    </section>
  </section>;

export default ContactDetails;
