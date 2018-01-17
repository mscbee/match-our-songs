import React, { Component } from 'react';
import './App.css';
import UsernameField from './components/UsernameField';
import Title from './components/Title';

class App extends Component {
  render() {
    return (
      <div>
        <Title />
        <UsernameField />
      </div>
    );
  }
}

export default App;
