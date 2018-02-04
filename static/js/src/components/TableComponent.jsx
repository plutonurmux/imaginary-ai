/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 04 February, 2018 @ 6:05 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

import React from 'react';

const TableComponent = (props) => {
  const rows = [];
  for (let i = 0; i < props.labels.length; i++) {
    const label = props.labels[i];
    const score = props.scores[i];
    rows.push(<tr key={i + 1}>
      <td>{i + 1}</td>
      <td>{label}</td>
      <td>{score}</td>
    </tr>);
  }

  let heading = props.heading.map(heading => <th key={heading}>{heading}</th>);
  heading = <tr>{heading}</tr>;

  return (
    <div className="table-wrapper">
      <table className="alt">
        <thead>{heading}</thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  );
};


export default TableComponent;