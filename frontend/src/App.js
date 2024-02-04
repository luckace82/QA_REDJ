import React, { Component } from 'react';

class App extends Component {
  constructor() {
    super();
    this.state = {
      questions: [],
    };
  }

  componentDidMount() {
    
    fetch('http://127.0.0.1:8000/Questions/')
      .then(response => response.json())
      
      
      }
      ;
  }



  
  

export default App;
