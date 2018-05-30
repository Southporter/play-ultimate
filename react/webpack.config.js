module.exports = {
	entry: {
		render: './render.jsx',
		gamesView: './entries/GamesView.jsx',
	},
	module: {
		rules: [
			{
				test: /\.(js|jsx)$/,
				exclude: /node_modules/,
				use: ['babel-loader']
			}
		]
	},
	resolve: {
		extensions: ['.js', '.jsx']
	},
	target: 'node',
	output: {
		path: __dirname + '/dist',
		publicPath: '/',
		filename: '[name].js'
	}
};
