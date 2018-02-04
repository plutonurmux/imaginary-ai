/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 04 February, 2018 @ 2:51 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React, {Component} from 'react';


class ContactForm extends Component {

  render() {
    return (
      <section>
        <form>
          <div className="field half first">
            <label htmlFor="name">Name</label>
            <input type="text" name="name" id="name"/>
          </div>
          <div className="field half">
            <label htmlFor="email">Email</label>
            <input type="text" name="email" id="email"/>
          </div>
          <div className="field">
            <label htmlFor="message">Message</label>
            <textarea name="message" id="message" rows="6"/>
          </div>
          <ul className="actions">
            <li>
              <input type="submit" value="Send Message" className="special"/>
            </li>
            <li>
              <input type="reset" value="Clear"/>
            </li>
          </ul>
        </form>
      </section>
    );
  }

}

export default ContactForm;
