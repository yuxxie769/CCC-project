<template>
  <div class="home view" id="home">
    <div class="jumbotron">
    </div>
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    // HelloWorld
  }
}
</script>

<style scoped>
  #home {
    background: url('../assets/313978.jpeg'); /* 换一张图片 */
    background-size: cover;
  }
</style>
