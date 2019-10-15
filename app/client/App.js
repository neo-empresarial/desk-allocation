import React, { Component } from 'react';
import './app.css';
import Table from './Table'

export default class App extends Component {
  constructor(props) {
    super(props);

    this.state = { data: null };
  }

  componentDidMount() {
    fetch('/api/getSchedule')
      .then(res => res.json())
      .then(res => {
        this.setState({ data: res });
      });
  }

  render() {

    if (!this.state.data) {
      return <div>Loading...</div>
    }

    return (
      <div>
        {this.state.data.map((day, idx) => <Table name={idx} data={day}></Table>)}
      </div>
    )
  }
}
