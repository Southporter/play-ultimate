import React, { Component } from 'react';

export default class GameCard extends Component {
	render() {
		const { game } = this.props;
		return (
			<div class="mdl-card mdl-shadow--4dp" style="width: 95%; margin-bottom: 2vw">
				<div class="mdl-card__title">
					<div class="flex-row" style="justify-content: space-between;">
						<div style="display: flex; flex-direction: column;">
							<h2 class="mdl-card__title-text">{game.name}</h2>
							<h4 class="mdl-card__subtitle-text">{game.location}</h4>
						</div>
						<div class="flex-column align-center">
							<div style="position: absolute; right: 38px; top: 30px">13</div>
							<i class="material-icons" style="font-size: 36px">calendar_today</i>
							<div>Tuesday</div>
						</div>
					</div>
				</div>
				<div
					class="mdl-card__actions mdl-card--border flex-row"
					style="justify-content: space-between;"
				>
					<button type="button" class="chip">
						<div class="mdl-color--green circle"></div>
						<span class="chip__text">I'm in</span>
					</button>
					<button type="button" class="chip" style="flex-direction: row-reverse">
						<div class="mdl-color--orange circle">{}</div>
						<div class="chip__text">I'm out</div>
					</button>
				</div>
			</div>
		);
	}
}
