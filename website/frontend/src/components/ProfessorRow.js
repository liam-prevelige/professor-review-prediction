/*
Output component for representing an professors's analysis 
*/

import React, { Component } from 'react';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash } from "@fortawesome/free-solid-svg-icons";

class ProfessorRow extends Component {
  render() {
    return (
      this.props.professors.map(row =>
        <div key={row.id}>
          <input
            type="result"
            name="name"
            value={row.name}
            readOnly
          />
          <input
            type="result"
            name="rating"
            value={row.rating}
            readOnly
          />
          <button className="delete-button" type="delete" onClick={event => this.props.handleDelete(event, row.name)}>
            <FontAwesomeIcon icon={faTrash} />
          </button>
        </div>
      )
    )
  }
}

export default ProfessorRow;