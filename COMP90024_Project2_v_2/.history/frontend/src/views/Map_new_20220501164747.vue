<template>
<div class="datamap view">
<div id="map"></div>
<div id="legend">
    <div class="title">{{ legendTitle }}</div>
    <div id="legendColors"></div>
</div>
<div class="footer">
    <div class="container">
    <div class="filters">
        <div class="input-group">
        <label class="input-group-text" for="sel_pla">Place</label>
        <select
            class="form-select"
            id="sel_pla"
            @change="switchPlace($event)"
        >
            <option v-for="place in places" :key="place" :value="place.n">
            {{ place.name }}
            </option>
        </select>
        </div>

        <div class="input-group">
        <label class="input-group-text" for="sel_sce">Twitter Data</label>
        <select
            class="form-select"
            id="sel_sce"
            @change="switchScenario($event)"
        >
            <option v-for="scenario in scenarios" :key="scenario">
            {{ scenario }}
            </option>
        </select>
        </div>

        <div class="input-group">
        <label class="input-group-text" for="sel_aur">Aurin Data</label>
        <select
            class="form-select"
            id="sel_aur"
            @change="switchAurin($event)"
        >
            <option v-for="aurin in aurins" :key="aurin">{{ aurin }}</option>
        </select>
        </div>
    </div>
    </div>
</div>
</div>
</template>

<script>
import { Loader } from "@googlemaps/js-api-loader";
import * as echarts from "echarts";



</script>

<style scoped>
.about {
position: absolute;
top: 0;
left: 0;
right: 0;
bottom: 0;
}

#map {
width: 100%;
height: 100%;
}

.footer {
position: absolute;
left: 0;
right: 0;
bottom: 0;
display: flex;
align-items: center;
justify-content: center;
height: 72px;
background: #ffffff70;
backdrop-filter: blur(5px);
}

.filters {
display: flex;
justify-content: space-between;
}

.filters > .input-group {
width: 30%;
}

#legend {
position: absolute;
left: 10px;
bottom: 82px;
height: 430px;
width: 78px;
padding: 0.5em;
background: #fff;
z-index: 1000;
display: flex;
flex-direction: column;
box-shadow: rgb(0 0 0 / 30%) 0px 1px 4px -1px;
}

#legend .title {
font-size: 12px;
text-align: center;
height: 36px;
display: flex;
align-items: center;
justify-content: center;
color: #333;
}

#legendColors {
display: flex;
flex: 1 1;
flex-direction: column;
}
</style>
<style>
div.gm-style-mtc,
button.gm-fullscreen-control {
top: 72px !important;
}
div.gmnoprint.gm-bundled-control.gm-bundled-control-on-bottom {
bottom: 152px !important;
}

#legendColors .subColor {
flex: 1;
display: inline-flex;
font-size: 12px;
align-items: center;
justify-content: center;
}

#legendColors .value {
color: #fff;
text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black
}
</style>
