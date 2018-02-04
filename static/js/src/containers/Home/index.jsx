/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 02 February, 2018 @ 12:17 AM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React, {Component} from 'react';

import Banner from '../../components/Banner';
import HomeListCard from '../../components/HomeListCard';
import InnerListItem from '../../components/InnerListItem'

import {PROJECT_LIST} from "../../constants/links";

const Home = (props) =>
  <div id="main">
    <Banner
      link="#one" link_text="Get Started" style="next scrolly"
      heading="Hi, my name is Victor"
      description={<p>I'm an Artificial Intelligence Engineer and researcher
        <br/> and here's a side piece of my works</p>}/>
    <section id="one" className="tiles">
      {PROJECT_LIST.map(item => <HomeListCard key={item.title} {...item} />)}
    </section>
    <section id="two">
      <InnerListItem
        title="A Language Model"
        link="/research/a-language-model" icon="next"
        description={<p>I discovered something which might lead to a major breakthrough in the field of A.I. and
          NLP <em>(Natural Language Processing)...</em> I did some math to see how it improves existing models
          and it was pretty damn good. It's on the topic of AI developing some abstract representation of
          concepts. I'm sorry if this doesn't makes sense but it's really a cool concepts which is what humans do
          unconsciously. I've always wanted to build and do sth amazing and meaningful for the whole world...</p>}
      />
    </section>
  </div>;

export default Home;
