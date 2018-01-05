"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 06 January, 2018 @ 12:19 AM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import redirect, url_for, request, escape, flash
from flask_mail import Mail, Message

from views import app

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'javafolabi@gmail.com'
app.config['MAIL_PASSWORD'] = 'itsprivate'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/contact/', methods=['POST'])
def contact():
    # Form elements
    name = escape(request.form['name'])
    email = escape(request.form['email'])
    message = escape(request.form['message'])
    # Message
    msg = Message(subject='Imaginary A.I. Contact form',
                  sender=(name, email),
                  recipients=['javafolabi@gmail.com'])
    msg.body = message
    mail.send(msg)
    flash('Message successfully sent')
    return redirect(url_for('index'))
