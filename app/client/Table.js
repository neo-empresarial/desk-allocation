import React, { Component } from 'react';
import PropTypes from 'prop-types';

import './Table.css';

class Table extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  renderTableRow() {
    const { data } = this.props;
    const hours = Object.keys(data);
    const rows = hours.map(hour => [...[hour], ...Object.values(data[hour])]);
    const table = rows.map((row, i) => (
      <tr key={row[0]}>
        {row.map((el, idx) => <td key={idx}>{el}</td>)}
      </tr>
    ));
    return table;
  }

  renderTableHeader() {
    const { data } = this.props;
    const header = [...[''], ...Object.keys(Object.values(data)[0])];
    return header.map((key, index) => (
      <th key={index}>{key.toUpperCase()}</th>
    ));
  }

  render() {
    const { weekdays, day } = this.props;

    return (
      <div>
        <h1 id="title">{weekdays[day]}</h1>
        <table id="solution">
          <thead>
            {this.renderTableHeader()}
          </thead>
          <tbody>
            {this.renderTableRow()}
          </tbody>
        </table>
      </div>
    );
  }
}

Table.propTypes = {
  day: PropTypes.number,
  weekdays: PropTypes.arrayOf(PropTypes.string),
  data: PropTypes.objectOf(PropTypes.arrayOf(PropTypes.string))
};

Table.defaultProps = {
  day: false,
  weekdays: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
  data: false
};

export default Table;
