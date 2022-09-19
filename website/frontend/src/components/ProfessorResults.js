/*
Output component for representing an professor's image & prediction results
*/

import React, { Component } from 'react';

class ProfessorResults extends Component {
  render() {
    return (
      this.props.last_analysis.map(row =>
        <div>
          <div className="result-string" style={{fontWeight: 'bold'}}>
            {row.name + " - " + row.rating}
          </div>
          <img
            src={row.url}
            alt="new"
            height={250}
          />
          <div className="result-string">
            {"• Happy? " + row.happy}
          </div>
          <div className="result-string">
            {"• Blurry? " + row.blur}
          </div>
          <div className="result-string">
            {"• Attractive? " + row.attractiveness}
          </div>
          <div className="result-string">
            {"• Colorful? " + row.colorfulness}
          </div>
        </div>
      )
    )
  }
}

export default ProfessorResults;