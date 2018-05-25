const render = require('./render.js').default;

function run(componentName, props) {
	console.debug(server);
	const html = server.render(componentName, props);
	console.log(html);
}

run(process.argv[2], process.argv[3]);
