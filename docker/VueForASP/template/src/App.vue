<template lang="pug">
#app
  h1 {{title}}
</template>

<script>

export default {
  name: 'App',
  data:function () {
    return{
      title:"Start here"
    }
  }
}
</script>

<style lang="sass" scoped>
.star
  color: red
</style>
