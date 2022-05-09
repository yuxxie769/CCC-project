<!-- Thanks COMP 90024 TEAM 68 Provide template Reference : https://github.com/CCC68/COMP90024_Project2, Hanzhen Yang 1070951, Hanzhong Wang, 1029740, Quan Zhou 1065302, Yuhang Xie 1089250, Ze Liu 1073628
Modoified By COMP90024 TEAM 45
Yingpei Ni 1252881
Yixue Jiang 1023137
Zirui Shan  1298781
Jinglin Li 1000797
Yuxiang Xie 1060196 -->
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
