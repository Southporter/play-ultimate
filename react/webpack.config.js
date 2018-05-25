module.exports = {
	entry: './render.jsx',
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
		path: __dirname,
		publicPath: '/',
		filename: 'render.js'
	}
};
