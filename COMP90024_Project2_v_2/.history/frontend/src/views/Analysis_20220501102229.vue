// Hanzhen Yang 1070951, 
// Hanzhong Wang, 1029740,
// Quan Zhou 1065302, 
// Yuhang Xie 1089250, 
// Ze Liu 1073628
<template>
  <div class="views">
    <div class="container">
      <h2 class="mt-5">Crime</h2>
      <div id="crime" style="width: 600px;height: 400px;"></div>
      <hr />
      <h2 class="mt-5">Dss_payment</h2>
      <div id="dss_payment" style="width: 600px;height: 400px;"></div>
      <hr />
      <h2 class="mt-5">Ndia_number</h2>
      <div id="ndia_number" style="width: 600px;height: 400px;"></div>
      <hr />
      <h2 class="mt-5">unsw_rental</h2>
      <div id="unsw_rental" style="width: 600px;height: 400px;"></div>
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
  },
  mounted() {
    this.fetch_NewData("data")
  },
  methods: {
    fetch_NewData(name) {
      fetch(`http://127.0.0.1:5000/analysis/${name}`)// fetch(`${process.env.VUE_APP_BACKEND_BASE_URL}analysis/${state}`)
        .then(function (response) {
          return response.json();
        })
        .then((jsonData) => {
            // console.log(jsonData);
            var data = jsonData["docs"]
            // console.log(data)
            this.init_NewBarChart(data, "crime", "crime");
            this.init_NewBarChart(data, "dss_payment", "dss_payment");
            this.init_NewBarChart(data, "ndia_number", "ndia_number");
            this.init_NewBarChart(data, "unsw_rental", "unsw_rental");
        //   console(jsonData)
        //   this[crime] = jsonData.crime;
        //   this.initBarChart(state, "population");
        //   this.initBarChart(state, "income");
        //   this.initBarChart(state, "obesity");
        });
    },
    
    // Crime 图
    init_NewBarChart(data, features, html_label){
    // 基于准备好的dom，初始化echarts实例
      var myChart = echarts.init(document.getElementById(html_label));
      console.log(data)
    //   console.log(data["0"][features])
      var data_list = [] //[483, 206, 916, 986]
      var city_list = [] //['Melbourne', 'Sydney', 'Brisbane', 'Adelaide']
      var feature_list = [features]

      for(var key in data){
        //   console.log(key)
        //   console.log(data[key][features])
          var fea_num = data[key][features]
          var city = data[key]["city"]
          city_list.push(city)
          data_list.push(fea_num)
      }
      console.log(city_list)
    //   console.log(features)
    //   console.log("+++++",feature_list)
      // 指定图表的配置项和数据
      var option = {
        title: {
          text: features   //'crime'
        },
        tooltip: {},
        legend: {
          data: feature_list //['crime']
        },
        xAxis: {
          data: city_list//['Melbourne', 'Sydney', 'Brisbane', 'Adelaide']
        },
        yAxis: {},
        series: [
          {
            name: features,  //['crime']
            type: 'bar',
            data: data_list
          },
        //   {
        //     name: 'unemploy_num_sa',
        //     type: 'bar',
        //     data: [101, 227, 101, 204]
        //   },
        //   {
        //     name: 'unemploy_rate',
        //     type: 'bar',
        //     data: [556, 1181, 556, 1213]
        //   },
        ]
      };

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
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