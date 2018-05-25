import http from 'http';
import express from 'express';
import render from './render';

const ADDRESS = process.env.NODE_HOST;
const PORT = process.env.NODE_PORT;

const app = express();
const server = http.Server(app);

app.use(bodyParser.json({ limit: '10mb' }));

app.get('/', function (req, res) {
	res.end('Rendering...');
});

app.post('/render', function (req, res) {
	const url = req.body.url;

	const rendered = render(url);

	res.json({
		html: rendered.html,
	});
});
