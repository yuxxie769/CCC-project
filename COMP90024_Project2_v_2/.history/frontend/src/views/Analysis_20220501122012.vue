// Hanzhen Yang 1070951, 
// Hanzhong Wang, 1029740,
// Quan Zhou 1065302, 
// Yuhang Xie 1089250, 
// Ze Liu 1073628
<template>
  <div class="views">
    <div class="container">
      <h2 class="mt-5">Job & Income & Unemployment Rate</h2>
      <div id="job_income_unemployment" style="width: 600px;height: 400px;"></div> 
      <hr />
      <h2 class="mt-5">Population</h2>
      <div id="population_all" style="width: 600px;height: 400px;"></div> 
      <div id="population_density" style="width: 600px;height: 400px;"></div> 
      <hr />

      <h2 class="mt-5">Disability Help</h2>
      <div id="disability_help" style="width: 600px;height: 400px;"></div> 
      <hr />
      <h2 class="mt-5">RAI & Rental</h2>
      <div id="rai_rental" style="width: 600px;height: 400px;"></div> 
      <hr />
      <h2 class="mt-5">Crime & Disabled & Income & Rant</h2>
      <div id="crime_disabled_income_rant" style="width: 600px;height: 400px;"></div> 
      <hr />

      <!-- <h2 class="mt-5">Crime</h2>
      <div id="crime" style="width: 600px;height: 400px;"></div>
      <hr />
      <h2 class="mt-5">Dss_payment</h2>
      <div id="dss_payment" style="width: 600px;height: 400px;"></div>
      <hr />
      <h2 class="mt-5">Ndia_number</h2>
      <div id="ndia_number" style="width: 600px;height: 400px;"></div>
      <hr />
      <h2 class="mt-5">unsw_rental</h2>
      <div id="unsw_rental" style="width: 600px;height: 400px;"></div> -->
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
            // this.init_NewBarChart(data, "crime", "crime");
            this.init_multi_BarChar(data,['Job', 'Income', 'Unemployment Rate'],"job_income_unemployment");
            this.init_population_all_NewBarChart(data,"population_all")
            // this.init_population_density_NewBarChart(data,"population","population_density")
            // this.init_NewBarChart(data, "dss_payment", "dss_payment");
            // this.init_NewBarChart(data, "ndia_number", "ndia_number");
            // this.init_NewBarChart(data, "unsw_rental", "unsw_rental");
        //   console(jsonData)
        //   this[crime] = jsonData.crime;
        //   this.initBarChart(state, "population");
        //   this.initBarChart(state, "income");
        //   this.initBarChart(state, "obesity");
        });
    },
    // bar chart 图
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
        ]
      };

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
    },

    init_population_all_NewBarChart(data, html_label){
    // 基于准备好的dom，初始化echarts实例
      var myChart = echarts.init(document.getElementById(html_label));
      console.log(data)
    //   console.log(data["0"][features])
      var population_list = [] //[483, 206, 916, 986]
      var city_list = [] //['Melbourne', 'Sydney', 'Brisbane', 'Adelaide']
      var feature_list = ["Population"]

      for(var key in data){
        //   console.log(key)
        //   console.log(data[key][features])
          var fea_num = data[key]["abs_population"][1]
          var city = data[key]["city"]
          city_list.push(city)
          population_list.push(fea_num)
      }
      console.log(city_list)
    //   console.log(features)
    //   console.log("+++++",feature_list)
      // 指定图表的配置项和数据
      var option = {
        title: {
          text: "Population"   //'crime'
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
            name: ["Population"],  //['crime']
            type: 'bar',
            data: population_list
          },
        ]
      };

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
    },

    init_population_all_NewBarChart(data, html_label){
    // 基于准备好的dom，初始化echarts实例
      var myChart = echarts.init(document.getElementById(html_label));
      console.log(data)
    //   console.log(data["0"][features])
      var population_density_list = [] //[483, 206, 916, 986]
      var city_list = [] //['Melbourne', 'Sydney', 'Brisbane', 'Adelaide']
      var feature_list = ["Population Density"]

      for(var key in data){
        //   console.log(key)
        //   console.log(data[key][features])
          var fea_num = data[key]["abs_population"][2] / data[key]["abs_population"][0]
          var city = data[key]["city"]
          city_list.push(city)
          population_list.push(fea_num)
      }
      console.log(city_list)
    //   console.log(features)
    //   console.log("+++++",feature_list)
      // 指定图表的配置项和数据
      var option = {
        title: {
          text: "Population Density"   //'crime'
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
            name: ["Population Density"],  //['crime']
            type: 'bar',
            data: population_density_list
          },
        ]
      };

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
    },

    // Job & Income & Unemployment Rate图
    init_multi_BarChar(data, features, html_label){
      var app = {};
      var chartDom = document.getElementById(html_label);
      var myChart = echarts.init(chartDom);
      var option;

      const posList = [
        'left',
        'right',
        'top',
        'bottom',
        'inside',
        'insideTop',
        'insideLeft',
        'insideRight',
        'insideBottom',
        'insideTopLeft',
        'insideTopRight',
        'insideBottomLeft',
        'insideBottomRight'
      ];
      app.configParameters = {
        rotate: {
          min: -90,
          max: 90
        },
        align: {
          options: {
            left: 'left',
            center: 'center',
            right: 'right'
          }
        },
        verticalAlign: {
          options: {
            top: 'top',
            middle: 'middle',
            bottom: 'bottom'
          }
        },
        position: {
          options: posList.reduce(function (map, pos) {
            map[pos] = pos;
            return map;
          }, {})
        },
        distance: {
          min: 0,
          max: 100
        }
      };
      app.config = {
        rotate: 90,
        align: 'left',
        verticalAlign: 'middle',
        position: 'insideBottom',
        distance: 15,
        onChange: function () {
          const labelOption = {
            rotate: app.config.rotate,
            align: app.config.align,
            verticalAlign: app.config.verticalAlign,
            position: app.config.position,
            distance: app.config.distance
          };
          myChart.setOption({
            series: [
              {
                label: labelOption
              },
              {
                label: labelOption
              },
              {
                label: labelOption
              },
              {
                label: labelOption
              }
            ]
          });
        }
      };
      const labelOption = {
        show: true,
        position: app.config.position,
        distance: app.config.distance,
        align: app.config.align,
        verticalAlign: app.config.verticalAlign,
        rotate: app.config.rotate,
        formatter: '{c}  {name|{a}}',
        fontSize: 16,
        rich: {
          name: {}
        }
      };
      console.log(data)
      console.log(data["0"][features])
      var data_job_list = [] //[483, 206, 916, 986]
      var data_income_list = []
      var data_unemploy_list = []
      var city_list = [] //['Melbourne', 'Sydney', 'Brisbane', 'Adelaide']

      for(var key in data){
          var job_area = data[key]["abs_job"][0]
          var unemply_area = data[key]["dese_unemploy"][0]
          var each_job = data[key]["abs_job"][1] / job_area
          var each_income = data[key]["abs_job"][2] / job_area
          var each_unemploy = data[key]["dese_unemploy"][1] / unemply_area
          data_job_list.push(each_job)
          data_income_list.push(each_income)
          data_unemploy_list.push(each_unemploy)
          var city = data[key]["city"]
          city_list.push(city)
      }
      console.log(city_list)
      console.log(data_job_list)
      console.log(data_income_list)
      console.log(data_unemploy_list)
      option = {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          data: features //['Forest', 'Steppe', 'Desert', 'Wetland']
        },
        toolbox: {
          show: true,
          orient: 'vertical',
          left: 'right',
          top: 'center',
          feature: {
            mark: { show: true },
            dataView: { show: true, readOnly: false },
            magicType: { show: true, type: ['line', 'bar', 'stack'] },
            restore: { show: true },
            saveAsImage: { show: true }
          }
        },
        xAxis: [
          {
            type: 'category',
            axisTick: { show: false },
            data: city_list//['Melbourne', 'Sydney', 'Brisbane', 'Adelaide']//['2012', '2013', '2014', '2015', '2016']
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: 'Job',
            type: 'bar',
            barGap: 0,
            label: labelOption,
            emphasis: {
              focus: 'series'
            },
            data: data_job_list//[4033,4295,1018,2002]
          },
          {
            name: 'Income',
            type: 'bar',
            label: labelOption,
            emphasis: {
              focus: 'series'
            },
            data: data_income_list//[103, 167, 15, 29]
          },
          {
            name: 'Unemployment Rate',
            type: 'bar',
            label: labelOption,
            emphasis: {
              focus: 'series'
            },
            data: data_unemploy_list//[242627, 449900, 112910, 256574]
          },
        ]
      };
      option && myChart.setOption(option);
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