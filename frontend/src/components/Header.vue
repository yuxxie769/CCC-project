// Hanzhen Yang 1070951, 
// Hanzhong Wang, 1029740,
// Quan Zhou 1065302, 
// Yuhang Xie 1089250, 
// Ze Liu 1073628
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