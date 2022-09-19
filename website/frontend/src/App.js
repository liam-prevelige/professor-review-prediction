/*
Frontend framework for Professor Review Predictor

Given a photo of a Dartmouth Professor creates a prediction on a 
5-point scale for the quality of their teaching.

Created by Liam Prevelige, September 2022

Sends & receives information via API from MongoDB.
*/

import React, { Component } from 'react';
import './App.css';
import ProfessorRow from './components/ProfessorRow';
import NewProfessor from './components/NewProfessor';
import ProfessorResults from './components/ProfessorResults';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      // State information for new inputs into the list of professors
      name: '',
      image_url: '',

      professors: [],  // list of dictionaries for professors' name and prediction results
      last_analysis: [],  // dictionary for one professor and contextualized results
      professors_loading: false,
      analysis_loading: false
    };

    // Listeners for changes to form inputs
    this.handleNameChange = this.handleNameChange.bind(this);
    this.handleUrlChange = this.handleUrlChange.bind(this);
    // Listeners for respective button clicks
    this.handleAddProfessor = this.handleAddProfessor.bind(this);
    this.handleDelete = this.handleDelete.bind(this);
  }

  handleNameChange(event) {
    this.setState({ name: event.target.value });
  }
  handleUrlChange(event) {
    this.setState({ image_url: event.target.value });
  }

  async handleAddProfessor(event) {
    /* 
      Puts professor in DB, then requests updated professor list 
      If a duplicate name is entered, existing entry is overridden
    */
    event.preventDefault();
    this.setState({
      professors_loading: true,
    })
    await fetch('/addprofessor/' + this.state.name + '/' + this.state.image_url, {
      method: 'PUT'
    });
    this.getProfessors()
  }

  async handleDelete(event, name) {
    /* 
      Deletes professor from DB, then requests updated professor list 
    */
    event.preventDefault();
    this.setState({
      professors_loading: true,
      analysis_loading: true,
    })
    await fetch('/deleteprofessor/' + name, {
      method: 'DELETE'
    });
    this.getProfessors()
  }

  getProfessors() {
    /* 
      Fetches list of dictionaries of professors' name and predicted review rating from DB
    */
    fetch('/getprofessors/')
      .then(response => response.json())
      .then(json => {
        this.setState({
          name: '',
          image_url: '',
          professors: json,
          professors_loading: false
        })
      })
    this.getLastAnalysis()
  }

  getLastAnalysis() {
    /* 
      Fetches last analysis with details
    */
    fetch('/getlastanalysis/')
      .then(response => response.json())
      .then(json => {
        this.setState({
          name: '',
          image_url: '',
          last_analysis: json,
          analysis_loading: false
        })
      })
  }

  componentDidMount() {
    this.getProfessors();
  }

  render() {
    return (
      <div className="App">
        <div className="app-title">Professor Review Predictor</div>
        <div className="app-description">(Poorly) Predict a Dartmouth professor's teaching reviews using nothing but their picture.</div>
        <div className="app-description">Uses React, Python, Flask, MongoDB, Machine Learning, and Statistical Analysis.</div>
        <div className="rowC">
          {/* Start of input column */}
          <div className="Inputs-col">
            <span className="col-title">Professor Predictions</span>
            <div className="inputs-body">
              <div>
                <span className="subtitle">Add Prediction</span>
                <NewProfessor handleNameChange={this.handleNameChange} handleUrlChange={this.handleUrlChange} handleAddProfessor={this.handleAddProfessor} name={this.state.name} image_url={this.state.image_url} />
                {this.state.professors_loading ? <span className="subtitle">Loading</span> : <ProfessorRow handleDelete={this.handleDelete} {...this.state} />}
              </div>
            </div>
          </div>
          {/* Start of results column */}
          <div className="Results-col">
            <span className="col-title">Analysis</span>
            <div className="results-body">
              <div>
                {this.state.analysis_loading ? <span className="subtitle">Loading</span> : <ProfessorResults {...this.state} />}
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;