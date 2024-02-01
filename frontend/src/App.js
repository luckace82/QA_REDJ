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
      .then(data => console.log(data))
      
      }
      ;
  }



    return (
      <div className='App'>
        {this.state.questions.map((question) => (
          <h1 key={question.id}>{question.question_txt}</h1>
        ))}
      </div>
    );
  

export default App;
