/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 02 February, 2018 @ 10:37 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import Generic from "../../components/Layouts/Generic";
import PreviewComponent from "../../components/PreviewComponent";
import TableComponent from "../../components/TableComponent";
import FileForm from "../../components/Forms/FileForm";

class ImageSearch extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Generic title="Image Search">
        <p>A computer system for browsing, searching and retrieving images from a large
          database of <Link to="https://en.wikipedia.org/wiki/Digital_image" target="_blank">digital images. </Link>
          Most traditional and common methods of image retrieval utilize some method of adding <Link
            to="https://en.wikipedia.org/wiki/Metadata" target="_blank">metadata</Link> such as
          captioning, keywords, or descriptions to the images so that retrieval can be performed over the annotation
          words. Manual image annotation is time-consuming, laborious and expensive; to address this, there has been
          a large amount of research done on <Link to="https://en.wikipedia.org/wiki/Automatic_image_annotation"
                                                   target="_blank">automatic image annotation.</Link> Additionally,
          the increase in social <Link to="https://en.wikipedia.org/wiki/Web_application"
                                       target="_blank">web
            applications</Link> and the <Link to="https://en.wikipedia.org/wiki/Semantic_web" target="_blank">
            semantic web</Link> have inspired the development of several web-based
          image annotation tools.</p>
        <form encType="multipart/form-data" id="image-search-form">
          <div className="row uniform">
            <div className="5u 12u$(medium)">
              <div className="input-group mb-3">
                <div className="input-group-prepend">
                  <button className="button special icon fa-search">Search</button>
                </div>
                <input type="text" placeholder="Enter Image URL" className="form-control"
                       aria-label="Image URL" aria-describedby="image-url"/>
              </div>
            </div>
            <div style={{textAlign: 'center'}} className="2u 12u$(medium)">
              <h4>OR</h4>
            </div>
            <div className="5u 12u$(medium)">
              <FileForm value="Search" inputName="image" hint="upload image"/>
            </div>
          </div>
        </form>

        <div className="row 200%">
          {/*Preview and scores*/}
          <div className="6u 12u$(medium)">
            <PreviewComponent title="Basketball with 82.54% accuracy." image="/static/images/pic03.jpg"/>
            {/*Top results & accuracy*/}
            <h4>Top (5) Matches</h4>
            <TableComponent
              heading={['Rank', 'Image class', 'Score']}
              labels={['Reinforcement learning', 'Temporal Difference learning', 'Deep learning']}
              scores={['90%', '5%', '5%']}/>
          </div>
          {/* Search results */}
          <div className="6u$ 12u$(medium)">
            <div className="row uniform">
              <h3>Search results for Victor I. Afolabi</h3>
              <div className="alt">
                {/*Results*/}
                <div className="row 50% uniform">
                  <div className="alt">
                    <h4><Link to="">Victor I. Afolabi</Link></h4>
                    <i>https://github.com/victor-iyiola</i>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci, aliquam aut enim incidunt
                      ipsam iure laborum, nemo neque nesciunt, optio possimus temporibus tenetur vitae voluptate
                      voluptatibus! Accusamus eveniet, ratione? Animi?</p>
                  </div>
                  <div className="alt">
                    <h4><Link to="">Victor I. Afolabi</Link></h4>
                    <i>https://github.com/victor-iyiola</i>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci, aliquam aut enim incidunt
                      ipsam iure laborum, nemo neque nesciunt, optio possimus temporibus tenetur vitae voluptate
                      voluptatibus! Accusamus eveniet, ratione? Animi?</p>
                  </div>
                  <div className="alt">
                    <h4><Link to="">Victor I. Afolabi</Link></h4>
                    <i>https://github.com/victor-iyiola</i>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci, aliquam aut enim incidunt
                      ipsam iure laborum, nemo neque nesciunt, optio possimus temporibus tenetur vitae voluptate
                      voluptatibus! Accusamus eveniet, ratione? Animi?</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Generic>
    );
  }
}

export default ImageSearch;

/*
    <!-- Search results -->
    <div className="6u$ 12u$(medium)">
      {% if data and data['search_results'] %}
        <div className="row uniform">
          <h3>Search results for {{ data['predictions']['top']['label'] }}</h3>
          <div className="alt">
             Results
            <div className="row 50% uniform">
              {% for _ in range(data['search_results']['titles']|count) -%}
                {% set search = data['search_results'] %}
                <h4>
                  <a href="{{ search['links'][loop.index0] }}">{{ search['titles'][loop.index0] }}</a>
                </h4>
                 <i>{{ search['cites'][loop.index0] }}</i>
                <p>{{ search['descriptions'][loop.index0] }}</p>
              {%- endfor %}
            </div>
          </div>
        </div>
      {% endif %}
    </div>

  </div>
 */
