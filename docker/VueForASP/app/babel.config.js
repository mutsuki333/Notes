module.exports = {
  presets: [
    '@vue/cli-plugin-babel/preset'
  ],
  "plugins": [
    [
      "component",
      {
        "libraryName": "element-ui",
        ext: ".scss",
        styleLibraryName: "../packages/theme-chalk/src"
      }
    ]
  ]
}
