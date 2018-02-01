/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 01 February, 2018 @ 2:15 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

const webpack = require('webpack');

const config = {

  entry: './js/src/index.jsx',

  output: {
    path: __dirname + '/js/dist',
    filename: 'bundle.js',
  },

  resolve: {
    extensions: ['.js', '.jsx', '.css']
  },

  module: {
    rules: [
      {
        test: /\.jsx?/,
        exclude: /node_modules/,
        use: 'babel-loader'
      }
    ]
  }

};

module.exports = config;
