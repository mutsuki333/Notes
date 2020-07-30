<template lang="pug">
#app
  el-button(type="success" round) test
  el-select
    el-option(label="v1" value="v1")
    el-option(label="v1" value="v1")
    el-option(label="v1" value="v1")
</template>

<script>

export default {
  name: 'App'
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
