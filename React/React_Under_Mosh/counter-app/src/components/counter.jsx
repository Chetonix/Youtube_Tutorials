import React, { Component } from "react";
class Counter extends React.Component {
  state = {
    value: this.props.value,
    tags: ["tag1", "tag2", "tag3"],
  };
  constructor() {
    super();
    //this.handleIncrement = this.handleIncrement.bind(this);
  }

  //could have used arrow notation to be able for 'this' to work below:
  handleIncrement = (product) => {
    // console.log("Increment Clicked!", this);
    // console.log(this.state);
    //console.log(product);
    this.setState({ value: this.state.value + 1 });
  };
  // styles = { fontSize: 10, color: "grey" };
  renderTags() {
    if (this.state.tags.length === 0) return <p>There are no tags!</p>;

    return (
      <ul>
        {this.state.tags.map((tag) => (
          <li key={tag}>{tag}</li>
        ))}
      </ul>
    );
  }

  render() {
    return (
      <div>
        <span className={this.getBadgeClasses()}>{this.formatCount()}</span>
        <button
          onClick={() => this.handleIncrement({ id: 1 })}
          className="btn btn-secondary btn-sm"
        >
          Increment
        </button>
        {this.renderTags()};
      </div>
    );
  }

  getBadgeClasses() {
    let classes = "badge m-2 bg-";
    classes += this.state.value === 0 ? "warning" : "primary";
    return classes;
  }

  formatCount() {
    const { value } = this.state;
    return value === 0 ? "Zero" : value;
  }
}

export default Counter;
