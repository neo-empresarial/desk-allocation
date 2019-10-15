import React, { Component } from 'react'
import './Table.css'

class Table extends Component {
  constructor(props) {
    super(props) //since we are extending class Table so we have to use super in order to override Component class constructor
    this.hours = Object.keys(this.props.data)
    this.days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
  }

  renderTableRow() {
    let rows = this.hours.map((hour) => [...[hour], ...Object.values(this.props.data[hour])])
    return rows.map((row, i) => <tr key={i}>{row.map((el, idx) => <td key={idx}>{el}</td>)}</tr>)
  }

  renderTableHeader() {
    let header = [...[''], ...Object.keys(Object.values(this.props.data)[0])]
    return header.map((key, index) => {
      return <td key={index}>{key.toUpperCase()}</td>
    })
  }

  render() {
    return (
      <div>
        <h1 id='title'>{this.days[this.props.name]}</h1>
        <table id='solution'>
          <thead>
            {this.renderTableHeader()}
          </thead>
          <tbody>
            {this.renderTableRow()}
          </tbody>
        </table>
      </div>
    )
  }
}

export default Table