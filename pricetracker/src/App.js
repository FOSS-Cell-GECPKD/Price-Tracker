import React, { Component } from 'react'
import './App.css'
import Navbar from './components/layout/Navbar'
import Credentials from './components/layout/Credentials'

//class based component
class App extends Component {

  render() {
    return (
      <div className="App">
        <Navbar />
        <Credentials />
      </div>
    )
  }

}
export default App