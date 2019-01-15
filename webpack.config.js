const path = require('path');

const baseConfig = {
  mode: 'development',
  resolve: {
    extensions: ['.ts', '.js', '.tsx'],
  },
  devtool: "cheap-module-eval-source-map",
  module: {
    rules: [
      {
        test: /.tsx?/,
        loader: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
  stats: {
    builtAt: true,
    errors: false,
    warnings: false,
  },
};

const clientConfig = {
  entry: {
    web: './static/js/index.ts',
  },
  output: {
    path: path.resolve(__dirname, 'static', 'build', 'js'),
    filename: '[name].js',
    publicPath: '/static/build/js/',
  },
  resolve: {
    extensions: ['.ts', '.tsx', '.js'],
  },
    externals: {
    jquery: 'jQuery',
    'materialize-css': 'M',
  },
};

module.exports = Object.assign({}, baseConfig, clientConfig);
