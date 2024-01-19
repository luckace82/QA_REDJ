import React, { Component } from 'react';

class App extends Component {
  constructor() {
    super();
    this.state = {
      questions: [],
      loading: true,
    };
  }

  componentDidMount() {
    console.log('Fetching data from API...');
    fetch('http://127.0.0.1:8000/Questions/')
      .then(response => response.json())
      .then(data => {
        console.log('Data from API:', data);
        this.setState({ questions: data, loading: false });
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        this.setState({ loading: false });
      });
  }

  componentDidUpdate(prevProps, prevState) {
    // Check if the questions array has changed
    if (prevState.questions !== this.state.questions) {
      console.log('Questions in state:', this.state.questions);
    }
  }

  render() {
    // Check if the data is still being fetched or if the array is empty
    if (this.state.loading) {
      return <p>Loading...</p>; // You can replace this with a loading indicator or message
    }

    return (
      <>
        {this.state.questions.map((question) => (
          <h1 key={question.id}>{question.question_txt}</h1>
        ))}
      </>
    );
  }
}

export default App;
