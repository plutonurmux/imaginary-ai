/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 02 February, 2018 @ 10:10 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';

import Generic from "../../components/Layouts/Generic";

const ALanguageModel = () => {
  return (
    <Generic title="A Language Model">
      A language model.
    </Generic>
  );
};

export default ALanguageModel;

/*
  <!-- Main -->
  <div id="main" className="alt">
    <div className="inner">
      <header className="major">
        <h1>A Language Model</h1>
      </header>
      - Background study
      <h3>Some Background Knowledge</h3>
      <div className="row">
        <div className="">
          <h4>What we Already Know</h4>
          <ul>
            <li>
              We already have AI models that generates realistic images from just text, they are called GANs (or
              Generative Adversarial Networks). The important thing to note about this model is that it's an
              unsupervised learning algorithm. i.e. it trains with no label what so ever... You just give it (the GAN) a
              phrase or caption, and then it outputs image which matches the caption you gave it.
            </li>
            <li>
              There are also models that takes as inputs images and produces a caption of what's going on in that
              image... <em>(TLDR; Convolutional Neural Network + Dynamic Memory Augmented Networks).</em>
            </li>
          </ul>
        </div>
      </div>

      - The model
      <h3>The Model</h3>
      <dl>
        <dt>My Inception</dt>
        <dd>
          <p>
            The way human understands concepts is that they build an abstract representation of event. for example if I
            tell you "I fell into a ditch last week" You probably pictured me walking then suddenly falling, right?
            Good. Hold on to that thought.
          </p>
        </dd>

        <dt>How it will work</dt>
        <dd>
          <p>
            Now an AI who's trying to understand a piece of text or news article. After feeding in the news article, the
            model starts phrase by phrase and then converts that phrase into images and then converts those images back
            into text.
          </p>
          <p>
            Okay, let me take it slowly. The images generated from the raw news article is the abstract event you were
            creating in your head when I said I fell into a ditch and then the image to text conversion is now you
            understanding what I said, and then you probably said "sorry".
            Human beings do this every sec of every day.
          </p>
        </dd>
      </dl>
      - Advantages
      <div className="row">
        <div className="">
          <h4>What is the real world use-case and Advantages</h4>
          <ol>
            <li>
              A bot can read through Wikipedia articles and give an accurate summary of what it learned from that
              article.
            </li>
            <li>
              We can turn it into a domain expert, i.e we train it to recognize financial patterns, then it will easily
              give us insights on what it thinks and so on.
            </li>
            <li>
              Building abstract representation of concepts and then going one step further to summarize what it just
              built is gonna give scientist insights as to how these models work.
            </li>
            <li>
              This could be applied to any domain, hence it's an AGI (Artificial General Intelligent) system.
            </li>
            <li>
              It is an unsupervised learning (which is a good news).
            </li>
          </ol>
        </div>
      </div>
      - Disadvantages
      <div className="row">
        <div className="">
          <h4>Disadvantages</h4>
          <ol>
            <li>
              It'll take longer to train.
            </li>
            <li>
              Some words are ambiguous. e.g (It'll take longer to train might mean sth else to. It could be constructing
              a train(the transport) rather than train(learning or discipline).
            </li>
          </ol>
        </div>
      </div>
      - Futher research
      <div className="row">
        <div className="">
          <h4>Further Research</h4>
          <ol>
            <li>
              There needs to be ways to know when to add to existing abstractions and not create new abstractions every
              time.
            </li>
            <li>
              It needs to somehow assign weights to these abstractions to know which one contributes more in a context.
            </li>
            <li>
              Faster training.
            </li>
          </ol>
        </div>
      </div>
    </div>
  </div>
 */