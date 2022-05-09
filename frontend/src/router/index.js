// Thanks COMP 90024 TEAM 68 Provide template Reference : https://github.com/CCC68/COMP90024_Project2, Hanzhen Yang 1070951, Hanzhong Wang, 1029740, Quan Zhou 1065302, Yuhang Xie 1089250, Ze Liu 1073628
// Modoified By COMP90024 TEAM 45
// Yingpei Ni 1252881
// Yixue Jiang 1023137
// Zirui Shan  1298781
// Jinglin Li 1000797
// Yuxiang Xie 1060196

import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/map',
    name: 'Map',
    component: () => import('../views/Map.vue')
  },
  {
    path: '/analysis',
    name: 'Analysis',
    component: () => import('../views/Analysis.vue')
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
