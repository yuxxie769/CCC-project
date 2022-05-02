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