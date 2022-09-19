/*
Input component for adding a new professor to the review tool
*/

import React, { Component } from 'react';

class NewProfessor extends Component {
  render() {
    return (
      <div>
        <form onSubmit={this.props.handleAddProfessor}>
          <input
            type="text"
            name="name"
            value={this.props.name}
            onChange={this.props.handleNameChange}
            placeholder="Name"
            autoFocus
          />
          <input
            type="text"
            name="image_url"
            value={this.props.image_url}
            onChange={this.props.handleUrlChange}
            placeholder="Image URL"
            autoFocus
          />
          <button className="add-professor-button" type="submit">Add Professor</button>
        </form>
      </div>
    )
  }
}

export default NewProfessor;