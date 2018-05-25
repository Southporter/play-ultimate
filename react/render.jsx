import React from 'react';
import ReactDOMServer from 'react-dom/server';
import containers from './containers';

function render(url, props) {
	const parsedProps = typeof props === 'string' ? JSON.parse(props) : props;
	const Component = containers[url];
	const html = ReactDOMServer.renderToString(
		<Component {...parsedProps} />
	);
	console.log(html);
}

render(process.argv[2], process.argv[3]);
