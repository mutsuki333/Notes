module.exports = {
  // css: {
  //   extract: false
  // },
  filenameHashing: false,
  productionSourceMap: false,
  publicPath:"./dist",
  configureWebpack:{
    optimization: {
      splitChunks: false
    },
  },
  chainWebpack: config => {
    config.module
    .rule('fonts')
      .use('url-loader')
        .tap((args) => {
          // Flatten fonts output: ./fonts/* -> ./*
          args.fallback.options.name = './dist/[name].[ext]';
          return args;
        })
        .end()
      .end()
    .end();
  }
}