/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 02 February, 2018 @ 10:13 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React, {Component} from 'react';

import Generic from "../../components/Layouts/Generic";
import TableComponent from "../../components/TableComponent";
import PreviewComponent from "../../components/PreviewComponent";
import SelectUploadForm from "../../components/Datasets/SelectUploadForm";
import ImageGridComponent from "../../components/ImageGridComponent";


class ImageClassification extends Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Generic title="Image Classification">
        <p>Image classification analyzes the numerical properties of various image features and
          organizes data into categories. Classification algorithms typically employ two phases of processing:
          <em>training</em> and <em>testing.</em> In the initial training phase, characteristic properties of
          typical image features are isolated and, based on these, a unique description of each classification
          category, i.e. <em>training class</em>, is created. In the subsequent testing phase, these feature-space
          partitions are used to classify image features.</p>
        <div className="caution">
          <h4><i className="fa fa fa-exclamation-circle"/> CAUTION </h4>
          <blockquote>
            Your dataset to be uploaded must be a <code>.zip</code> file & the
            directory must contain the class labels whereas the class labels holds all the images for that class.
          </blockquote>
        </div>

        {/* Previews & Datasets */}
        <div className="row 200%">
          {/* Preview & Score */}
          <div className="6u 12u$(medium)">
            <PreviewComponent title="Preview Image" image="/static/images/pic03.jpg"/>
            <h4>Top (5) Matches.</h4>
            <TableComponent
              heading={['Rank', 'Image class', 'Score']}
              labels={['Reinforcement learning', 'Temporal Difference learning', 'Deep learning']}
              scores={['90%', '5%', '5%']}/>
          </div>
          {/* Datasets */}
          <div className="6u$ 12u$(medium)">
            <div className="row uniform">
              <div>
                {/* Dataset options*/}
                <SelectUploadForm
                  title="Dataset Options"
                  options={[{value: '101-dataset', text: '101 Dataset'}, {value: 'pokemon', text: 'Pokemon'}]}
                  trainName="train" uploadName="upload" inputName="dataset"/>
                {/* Dataset contents */}
                <div className="12u$">
                  <h3>101 Objects Categories</h3>
                  <ImageGridComponent
                    images={['/static/images/pic08.jpg', '/static/images/pic09.jpg', '/static/images/pic10.jpg',
                      '/static/images/pic09.jpg', '/static/images/pic08.jpg', '/static/images/pic09.jpg',
                      '/static/images/pic10.jpg', '/static/images/pic10.jpg', '/static/images/pic08.jpg',]}/>
                </div>
              </div>
            </div>
          </div>
        </div>

      </Generic>
    );
  }

}

export default ImageClassification;
