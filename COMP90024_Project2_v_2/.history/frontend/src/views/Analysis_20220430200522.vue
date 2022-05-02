// Hanzhen Yang 1070951, 
// Hanzhong Wang, 1029740,
// Quan Zhou 1065302, 
// Yuhang Xie 1089250, 
// Ze Liu 1073628
<template>
  <div class="views">
    <div class="container">
      <!-- <h1>Aurin Data</h1> -->
      <h2 class="mt-5">Population</h2>
      <div id="vic_population_bar" class="bar_chart mt-5"></div>
      <div id="nsw_population_bar" class="bar_chart mt-3"></div>
      <!-- <div id="population_boxplot" class="bar_chart mt-3"></div> -->
      <hr />
      <h2 class="mt-5">Income</h2>
      <div id="vic_income_bar" class="bar_chart mt-5"></div>
      <div id="nsw_income_bar" class="bar_chart mt-3"></div>
      <hr />
      <h2 class="mt-5">Obesity Rate</h2>
      <div id="vic_obesity_bar" class="bar_chart mt-5"></div>
      <div id="nsw_obesity_bar" class="bar_chart mt-3"></div>
    </div>
  </div>
</template>
<script>
import * as echarts from "echarts";
export default {
  setup() {},
  data() {
    return {
      vic: null,
      nsw: null,
      aurin: {
        population: "population",
        income: "income_2014",
        obesity: "obesity_rate",
      },
    };
  },
  watch: {},
  beforeMount() {
    // this.fetchData("nsw");
  },
  mounted() {
    this.fetchData("vic");
    this.fetchData("nsw");
  },
  methods: {
    fetchData(state) {
      fetch(`${process.env.VUE_APP_BACKEND_BASE_URL}analysis/${state}`)
        .then(function (response) {
          return response.json();
        })
        .then((jsonData) => {
          console.log(process.env.VUE_APP_BACKEND_BASE_URL);
          this[state] = jsonData.features;
          this.initBarChart(state, "population");
          this.initBarChart(state, "income");
          this.initBarChart(state, "obesity");
        });
    },
    initBarChart(state, dataset) {
      let stateFullName = this.$store.state.places[state].name;
      let [x, y] = [[], []];
      let key = this.aurin[dataset];
      this[state].forEach((feature) => {
        let value = feature.properties[key];
        if (!value) {
          return true;
        }
        let name = feature.properties[`${state}_lga__3`];
        x.push(name);
        y.push(
          dataset !== "obesity"
            ? value
            : ((value / feature.properties.population) * 100).toFixed(4)
        );
      });
      console.log(`${state}_${dataset}_bar`);
      var chartDom = document.getElementById(`${state}_${dataset}_bar`);
      var myChart = echarts.init(chartDom);
      var option;

      let title = {
        income: `The Median Income of ${stateFullName} Residents in 2014`,
        population: `The Population in Each Local Government Area of ${stateFullName}`,
        obesity: `The Obesity Rate of People over 18 years old in ${stateFullName}`,
      };

      let color = {
        income: "#5470c6",
        population: "#ffc107",
        obesity: "#20c997",
      };

      option = {
        title: {
          text: title[dataset],
          left: "center",
        },
        color: color[dataset],
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
          formatter: function (params) {
            var tar = params[0];
            let tip = {
              income: `${tar.name}<br/>AUD $${tar.value}`,
              population: `${tar.name}<br/>${tar.value}`,
              obesity: `${tar.name}<br/>${tar.value}%`,
            };
            return tip[dataset];
          },
        },
        grid: {
          top: "10%",
          bottom: "30%",
        },
        xAxis: {
          type: "category",
          data: x,
          axisLabel: {
            interval: 0,
            rotate: 45,
          },
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            data: y,
            type: "bar",
            showBackground: false,
            backgroundStyle: {
              color: "rgba(180, 180, 180, 0.2)",
            },
          },
        ],
        dataZoom: [
          {
            show: true,
            realtime: true,
            start: 0,
            end: 30,
          },
        ],
      };

      option && myChart.setOption(option);
    },
    initBoxplot() {
     
    },
  },
};
</script>
<style scoped>
.bar_chart {
  width: 100%;
  height: 600px;
}
</style>