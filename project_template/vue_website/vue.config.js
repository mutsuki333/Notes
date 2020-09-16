module.exports = {
  filenameHashing: false,
  publicPath: process.env.NODE_ENV === 'production'
    ? '/admin/'
    : '/',
  productionSourceMap: false,
  pluginOptions: {
    i18n: {
      locale: 'zh-tw',
      fallbackLocale: 'zh-tw',
      localeDir: 'locales',
      enableInSFC: true
    }
  }
}
