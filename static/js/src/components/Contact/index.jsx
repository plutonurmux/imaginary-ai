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

import ContactForm from './ContactForm';
import ContactDetails from './ContactDetails';


const Contact = () =>
  <section id="contact">
    <div className="inner">
      <ContactForm/>
      <ContactDetails/>
    </div>
  </section>;

export default Contact;
