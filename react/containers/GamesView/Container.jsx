import React, { Component } from 'react';
import Card from './GameCard';

export default class Container extends Component {
	renderCards() {
		const { games, gameDays } = this.props;
		const parsed = typeof gameDays === 'string' ?
			JSON.parse(gameDays) : gameDays;
		console.error('parsed', parsed);
		const parsedGames = typeof games === 'string' ? JSON.parse(games) : games;
		return parsed.map(gameDay => <Card day={gameDay} games={parsedGames} />);
	}
	render() {
		return (
			<div>
				{this.renderCards()}
			</div>
		);
	}
}
