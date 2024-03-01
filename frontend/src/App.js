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
      .then(data => {
        // Update the state with the fetched questions
        this.setState({ questions: data });
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }

  render() {
    const { questions } = this.state;

    return (
      <div>
        <h1>Questions</h1>
        <ul>
          {questions.map(question => (
            <li key={question.id}>{question.question_txt}</li>
          ))}
        </ul>
      </div>
    );
  }
}

export default App;
