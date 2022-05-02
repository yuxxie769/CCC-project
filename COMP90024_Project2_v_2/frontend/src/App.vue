<template>
  <div>
    <header id="nav" class="p-3 text-white d-flex">
      <div class="container">
        <div class="d-flex flex-wrap align-items-center">
          <span class="me-md-auto">TEAM 45</span>
          <ul class="nav">
            <router-link
              v-for="route in routes"
              class="nav-link text-white"
              :to="route.path"
              :key="route.name"
            >
              {{ route.name }}
            </router-link>
          </ul>
        </div>
      </div>
    </header>
    <router-view />
  </div>
</template>
<script>
export default {
  setup() {},
  data() {
    return {
      routes: [],
    };
  },
  beforeMount() {
    this.routes = this.$router.options.routes;
    // console.log(this.$router)
  },
};
</script>
<style>
#nav {
  position: relative;
  z-index: 1000;
  backdrop-filter: blur(5px);
  background: #21252980;
}
.view {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 100;
}
</style>
