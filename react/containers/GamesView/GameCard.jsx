import React, { Component } from 'react';
import { array, object } from 'prop-types';

class GameCard extends Component {
	render() {
		const { day, games } = this.props;
		const game = games.find(game => game.pk === day.fields.game);
		return (
			<div
				className="mdl-card mdl-shadow--4dp"
				style={{ width: '95%', marginBottom: '2vw'}}
			>
				<div className="mdl-card__title">
					<div className="flex-row" style={{ justifyContent: 'space-between'}}>
						<div style={{ display: 'flex', flexDirection: 'column' }}>
							<h2 className="mdl-card__title-text">{game.fields.name}</h2>
							<h4 className="mdl-card__subtitle-text">{game.fields.location}</h4>
						</div>
						<div className="flex-column align-center">
							<div style={{ position: 'absolute', right: '38px', top: '30px' }}>13</div>
							<i className="material-icons" style={{ fontSize: '36px'}}>calendar_today</i>
							<div>Tuesday</div>
						</div>
					</div>
				</div>
				<div
					className="mdl-card__actions mdl-card--border flex-row"
					style={{ justifyContent: 'space-between', flexWrap: 'wrap' }}
				>
					<button type="button" className="chip">
						<div className="mdl-color--green circle">
							{ day.fields.attendees.length }
						</div>
						<span className="chip__text">I'm in</span>
					</button>
					<button type="button" className="chip" style={{ flexDirection: 'row-reverse' }}>
						<div className="mdl-color--orange circle">
							{ day.fields.non_attendees.length }
						</div>
						<div className="chip__text">I'm out</div>
					</button>
				</div>
			</div>
		);
	}
}

GameCard.propTypes = {
	games: array,
	day: object,
};

export default GameCard;
