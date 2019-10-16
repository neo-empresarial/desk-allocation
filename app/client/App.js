import React, { Component } from 'react';
import './app.css';
import Table from './Table';

export default class App extends Component {
  constructor(props) {
    super(props);

    this.state = { data: null };
  }

  componentDidMount() {
    fetch('/api/getSchedule')
      .then(res => res.json())
      .then((res) => {
        this.setState({ data: res });
      });
  }

  render() {
    const { data } = this.state;
    return (
      <div>
        {data
          ? data.map((day, idx) => <Table day={idx} data={day} />)
          : 'Loading...'}
      </div>
    );
  }
}
