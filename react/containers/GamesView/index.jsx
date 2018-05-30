import React, { Component } from 'react';
import Container from './Container';


export default class Wrapper extends Component {
	constructor(props) {
		super(props);

		this.state = {
			props,
		};
	}
	// componentDidMount() {
	// 	this.setState({ props: window.props });
	// }
	render() {
		return <Container props={this.state.props} />;
	}
}


