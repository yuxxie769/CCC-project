<!-- Thanks COMP 90024 TEAM 68 Provide template Reference : https://github.com/CCC68/COMP90024_Project2, Hanzhen Yang 1070951, Hanzhong Wang, 1029740, Quan Zhou 1065302, Yuhang Xie 1089250, Ze Liu 1073628
Modoified By COMP90024 TEAM 45.
(Sort alphabetically by family name.)
Yixue Jiang 1023137
Jinglin Li 1000797
Yingpei Ni 1252881
Zirui Shan 1298781
Yuxiang Xie 1060196 -->
<template>
    <div>
        <h1 v-bind:title="tips">{{ msg }}</h1>
        <input type="text" v-model="msg"/>
        
    </div>
</template>

<script>
export default {
    setup() {
        
    },
    data() {
        return {
            msg: 'Hello World',
            tips: 'This is a header'
        }
    }
}
</script>

<style scoped>

</style>