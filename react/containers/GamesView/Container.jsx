import React, { Component } from 'react';
import Card from './GameCard';

export default class Container extends Component {
	renderCards() {
		const { games } = this.props;
		const parsed = JSON.parse(games);
		return parsed.map(game => <Card game={game} />);
	}
	render() {
		return (
			<div>
				{this.renderCards()}
			</div>
		);
	}
}
