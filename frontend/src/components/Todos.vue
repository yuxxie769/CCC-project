// Hanzhen Yang 1070951, 
// Hanzhong Wang, 1029740,
// Quan Zhou 1065302, 
// Yuhang Xie 1089250, 
// Ze Liu 1073628
<template>
    <div>
        <h2 v-show="showHeader">Todo list</h2>
        <ul>
            <li v-for="todo in todos" :key="todo">
                {{todo.title}}
                <span v-if="todo.completed"> - done</span>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    setup() {
        
    },
    data() {
        return {
            showHeader: false,
            todos: [
                {title: "Todo task 1", completed: false},
                {title: "Todo task 2", completed: true},
                {title: "Todo task 3", completed: false}
            ]
        }
    }
}
</script>

<style scoped>
    li {
        text-align-last: left;
    }
</style>