<!-- Thanks COMP 90024 TEAM 68 Provide template Reference : https://github.com/CCC68/COMP90024_Project2, Hanzhen Yang 1070951, Hanzhong Wang, 1029740, Quan Zhou 1065302, Yuhang Xie 1089250, Ze Liu 1073628
Modoified By COMP90024 TEAM 45
Yingpei Ni 1252881
Yixue Jiang 1023137
Zirui Shan  1298781
Jinglin Li 1000797
Yuxiang Xie 1060196 -->
<template>
  <div class="views">
    <div class="container">
      <div class="center">
      <h4 class="mt-5">Character Selection</h4>      
      <button @click="tabChange" data-id="1">Crime</button>
      <button @click="tabChange" data-id="2">Income</button>
      <button @click="tabChange" data-id="3">Disabled</button>
      </div>
      <div v-show="tab==1">
      <h2 class="mt-5">Crime</h2>
      <p>Tweets With Crime Relate Key Words</p>
      <div id="twitter_crime" style="width: 800px;height: 500px;"></div> 
      <p>Aurin Population & Unemployment Data</p>
      <div id="Aruin_crime" style="width: 800px;height: 500px;"></div> 
      <p>Tweets With Crime Relate Key Words</p> 
      <div id="7_news_9_news" style="width: 800px;height: 500px;"></div> 
      <p>Emotion In Crime Related Tweets</p>
      <div id="Emotion" style="width: 800px;height: 500px;"></div>
      <p>Daily Crime Relate Tweets In Melbourne</p>
      <div id="Daily_crime_tweets_Melbourne" style="width: 800px;height: 500px;"></div> 
      <p>Total Crime Relate Tweets In 2019</p>
      <div id="Suburb" style="width: 800px;height: 500px;"></div> 
      <hr />
      </div>
      <div v-show="tab==2">
      <h2 class="mt-5">Income</h2>
      <p>Aurin RAI Score</p>
      <div id="rai" style="width: 800px;height: 500px;"></div> 
      <p>Twitter 7 Day Income & Rant</p>
      <div id="twitter_7_income_rant" style="width: 800px;height: 500px;"></div>
      <p>Aurin Rental Households number</p>
      <div id="rental" style="width: 800px;height: 500px;"></div>
      <p>Aurin Jobs Condition</p>
      <div id="Aurine_job_income" style="width: 800px;height: 500px;"></div>  
      <hr />
      </div>
      <div v-show="tab==3">
      <h2 class="mt-5">Disabled</h2>
      <p>Disabled Tweets</p>
      <div id="twitter_dis" style="width: 800px;height: 500px;"></div> 
      <p>Aurin Disabled Number</p>
      <div id="Aruin_ndia_number" style="width: 800px;height: 500px;"></div> 
      <p>Aurin Disabled Grant Received</p>
      <div id="Aruin_dss_payment" style="width: 800px;height: 500px;"></div> 
      <hr />
      </div>
    </div>
  </div>
</template>
<script>
import * as echarts from "echarts";
export default {
  setup() {},
  data() {
    return {
      tab: 1,
    };
  },
  watch: {},
  beforeMount() {
  },
  mounted() {
    this.fetch_NewData("data")
    this.fetch_suburb("suburb")
  },
  methods: {
    tabChange(e){
      let tabid = e.target.dataset.id
      this.tab = tabid
    },
    fetch_NewData(name) {
      fetch(`http://127.0.0.1:5000/analysis/${name}`)
        .then(function (response) {
          return response.json();
        })
        .then((jsonData) => {
            var data = jsonData["docs"]
            // Crime
            this.init_Multi_NewBarChart_Twitter_crime(data, "twitter_crime");
            this.init_Multi_NewBarChart_Aurin_crime(data, "Aruin_crime");
            this.init_7_9_crime(data,"7_news_9_news","7 News & 9 News");
            this.init_emotion_chart(data,"Emotion");
            this.init_daily_crime_melbourne(data, "Daily_crime_tweets_Melbourne")

            // Income
            this.init_multi_lineChar_RAI(data, "rai");
            this.init_multi_BarChat_income_rant(data,"twitter_7_income_rant", "Twitter")
            this.init_NewBarChart(data, "unsw_rental", "rental", "Aurin");
            this.init_multi_BarChat_job_income(data,"Aurine_job_income", "Aurine")

            // Disabled
            this.init_Multi_BarChart_diabled_7_30(data,"twitter_dis", "Twitter");
            this.init_NewBarChart(data, "ndia_number", "Aruin_ndia_number", "Aurin");
            this.init_NewBarChart(data, "dss_payment", "Aruin_dss_payment", "Aurin");            
        });
    },
    fetch_suburb(name){
      fetch(`http://127.0.0.1:5000/analysis/${name}`)
        .then(function (response) {
          return response.json();
        })
        .then((jsonData) => {
          var data = jsonData["docs"]
          this.init_suburb_pie_char(data,"Suburb")
        });
    },
    init_NewBarChart(data, features, html_label, text_name){
      var myChart = echarts.init(document.getElementById(html_label));

      var data_list = [] 
      var city_list = [] 
      var feature_list = [features]

      for(var key in data){
          var fea_num = data[key][features]
          var city = data[key]["city"]
          city_list.push(city)
          data_list.push(fea_num)
      }

      var option = {
        title: {
          text: text_name   
        },
        tooltip: {},
        legend: {
          data: feature_list 
        },
        xAxis: {
          data: city_list
        },
        yAxis: {},
        series: [
          {
            name: features,  
            type: 'bar',
            data: data_list
          },
        ]
      };
      myChart.setOption(option);
    },

    init_population_all_NewBarChart(data, html_label){
      var myChart = echarts.init(document.getElementById(html_label));

      var population_list = []
      var city_list = [] 
      var feature_list = ["Population"]

      for(var key in data){

          var fea_num = data[key]["abs_population"][1]
          var city = data[key]["city"]
          city_list.push(city)
          population_list.push(fea_num)
      }

      var option = {
        title: {
          text: "Population"   
        },
        tooltip: {},
        legend: {
          data: feature_list 
        },
        xAxis: {
          data: city_list
        },
        yAxis: {},
        series: [
          {
            name: ["Population"], 
            type: 'bar',
            data: population_list
          },
        ]
      };

      myChart.setOption(option);
    },

    init_population_density_NewBarChart(data, html_label){
      var myChart = echarts.init(document.getElementById(html_label));

      var population_density_list = []
      var city_list = [] 
      var feature_list = ["Population Density"]

      for(var key in data){
          var fea_num = data[key]["abs_population"][2] / data[key]["abs_population"][0]
          var city = data[key]["city"]
          city_list.push(city)
          population_density_list.push(fea_num)
      }

      var option = {
        title: {
          text: "Population Density" 
        },
        tooltip: {},
        legend: {
          data: feature_list 
        },
        xAxis: {
          data: city_list
        },
        yAxis: {},
        series: [
          {
            name: ["Population Density"],
            type: 'bar',
            data: population_density_list
          },
        ]
      };

      myChart.setOption(option);
    },
    init_multi_BarChat_income_rant(data, html_label, head_label){
      var chartDom = document.getElementById(html_label);
      var myChart = echarts.init(chartDom);
      var option;

      var data_rant_list = [] 
      var data_income_list = []
      var city_list = []

      for(var key in data){
          var each_income = data[key]["income"]
          var each_rant = data[key]["rant"]
          data_rant_list.push(each_rant)
          data_income_list.push(each_income)
          var city = data[key]["city"]
          city_list.push(city)
      }

      option = {
        title: {
          text: head_label 
        },
        legend: {
          data: ["income","rant"]
        },
        xAxis: {
          type: 'category',
          data: city_list
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            data: data_rant_list,
            name: "income",
            type: 'bar',
            showBackground: true,
            backgroundStyle: {
              color: 'rgba(180, 180, 180, 0.2)'
            }
          },
          {
            data: data_income_list,
            name: "rant",
            type: 'bar',
            showBackground: true,
            backgroundStyle: {
              color: 'rgba(180, 180, 180, 0.2)'
            }
          }
        ]
      };

      option && myChart.setOption(option);
    },
    init_multi_lineChar_RAI(data, html_label){
      var chartDom = document.getElementById(html_label);
      var myChart = echarts.init(chartDom);
      var option;

      var city_list = []
      var mel_list = []
      var syd_list = []
      var bris_list = []
      var adela_list = []

      for(var key in data){
          var city = data[key]["city"]
          var num_area = data[key]["sgsep_rai"][0]
          var Q1 = data[key]["sgsep_rai"][1] / num_area
          var Q2 = data[key]["sgsep_rai"][2] / num_area
          var Q3 = data[key]["sgsep_rai"][3] / num_area
          var Q4 = data[key]["sgsep_rai"][4] / num_area
          var temp_list = [Q1, Q2, Q3, Q4]

          city_list.push(city)
          if (city === "Melbourne"){
            mel_list = temp_list
          }else if(city === "Sydney"){
            syd_list = temp_list
          }else if(city === "Adelaide"){
            adela_list = temp_list
          }else{
            bris_list = temp_list
          }
      }
      option = {
        title: {
          text: 'RAI'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: city_list
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: ['First quarter', 'Second quarter', 'Third quarter', 'Fourth quarter']
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: "Melbourne", 
            type: 'line',
            stack: 'Total1',
            data: mel_list
          },
          {
            name: 'Sydney',
            type: 'line',
            stack: 'Total2',
            data: syd_list
          },
          {
            name: 'Brisbane',
            type: 'line',
            stack: 'Total3',
            data: bris_list
          },
          {
            name: 'Adelaide',
            type: 'line',
            stack: 'Total4',
            data: adela_list
          },
        ]
      };

      option && myChart.setOption(option);
    },

    init_Multi_NewBarChart_Twitter_crime(data, html_label){
      var myChart = echarts.init(document.getElementById(html_label));
      var crime_7_list = []
      var crime_30_list = []
      var city_list = [] 
      var features = "Twitter Crime"
      for(var key in data){
          var crime_7 = data[key]["crime"]
          var crime_30 = data[key]["crime_results_30days"]
          var city = data[key]["city"]
          city_list.push(city)
          crime_7_list.push(crime_7)
          crime_30_list.push(crime_30)
      }
      var option = {
        title: {
          text: features   
        },
        tooltip: {},
        legend: {
          data: ['7 days','30 days'] 
        },
        xAxis: {
          data: city_list
        },
        yAxis: {},
        series: [
          {
            name: '7 days',
            type: 'bar',
            data: crime_7_list
          },
          {
            name: '30 days',
            type: 'bar',
            data: crime_30_list
          },
        ]
      };

      myChart.setOption(option);
    },

    init_Multi_NewBarChart_Aurin_crime(data, html_label){
      var myChart = echarts.init(document.getElementById(html_label));
      var population_all_list = []
      var population_density_list = []
      var unemplyment = []
      var city_list = []
      var features = "Aurin Crime"

      for(var key in data){
          var  num_area = data[key]["abs_population"][0]
          var population_all = data[key]["abs_population"][1]
          var population_density = data[key]["abs_population"][2] / num_area
          var unemplyment_each = data[key]["dese_unemploy"][1] / data[key]["dese_unemploy"][0]
          var city = data[key]["city"]
          city_list.push(city)
          population_all_list.push(population_all)
          population_density_list.push(population_density)
          unemplyment.push(unemplyment_each)
      }
      var option = {
        title: {
          text: features 
        },
        tooltip: {},
        legend: {
          data: ['Population','Population Density', 'Unemployment Rate'] 
        },
        xAxis: {
          data: city_list
        },
        yAxis: {},
        series: [
          {
            name: 'Population',  
            type: 'bar',
            data: population_all_list
          },
          {
            name: 'Population Density',  
            type: 'bar',
            data: population_density_list
          },
          {
            name: 'Unemployment Rate',  
            type: 'bar',
            data: unemplyment
          },
        ]
      };

      myChart.setOption(option);
    },

    init_7_9_crime(data, html_label, text_name){
      var myChart = echarts.init(document.getElementById(html_label));
      var seven_list = []
      var nine_list = [] 
      var city_list = []
      var feature_list = ["7 news","9 news"]

      for(var key in data){
          var seven  = data[key]["news_time_line_7news"]
          var nine = data[key]["news_time_line_9news"]
          var city = data[key]["city"]
          city_list.push(city)
          nine_list.push(nine)
          seven_list.push(seven)
      }
      var option = {
        title: {
          text: text_name  
        },
        tooltip: {},
        legend: {
          data: feature_list 
        },
        xAxis: {
          data: city_list
        },
        yAxis: {},
        series: [
          {
            name: "7 news",  
            type: 'bar',
            data: seven_list
          },
          {
            name: "9 news", 
            type: 'bar',
            data: nine_list
          },
        ]
      }

      myChart.setOption(option);
    },

    init_emotion_chart(data,html_label){
      var chartDom = document.getElementById(html_label);
      var myChart = echarts.init(chartDom);
      var option;

      var emotion_list = {}

      for(var key in data){
          var emotion  = data[key]["emotion"]
          var city = data[key]["city"]
          emotion_list[city] = emotion
      }

      option = {
        title: {
          text: 'Emotion Crime'
        },
        tooltip: {},
        legend: {
          data: ['Melbourne', 'Sydney', 'Brisbane', 'Adelaide']
        },
        radar: {
          indicator: [
            { name: 'Happy', max: 400},
            { name: 'Angry', max: 400},
            { name: 'Surprise', max: 400},
            { name: 'Sad', max: 400},
            { name: 'Fear', max: 400},
          ]
        },
        series: [
          {
            name: 'Emotion Crime Tweets',
            type: 'radar',
            data: [
              {
                value: emotion_list['Melbourne'],
                name: 'Melbourne'
              },
              {
                value: emotion_list['Sydney'],
                name: 'Sydney'
              },
              {
                value: emotion_list['Brisbane'],
                name: 'Brisbane'
              },
              {
                value: emotion_list['Adelaide'],
                name: 'Adelaide'
              }
            ]
          }
        ]
      };

      option && myChart.setOption(option);
    },

    // suburb
    init_suburb_pie_char(data, html_label){
      var chartDom = document.getElementById(html_label);
      var myChart = echarts.init(chartDom);
      var option;
      
    var crime_list = {} 

      for(var key in data){
          var crime = data[key]["crime_suburb"]
          var city = data[key]["city"]
          crime_list[city] = crime
      }
      option = {
        title: {
          text: 'Suburb',
          subtext: 'Total Crime Relative Tweets In 2019',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: 'left'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            data: [
              { value: crime_list["Melbourne City"], name: 'Melbourne City' },
              { value: crime_list["Richmond"], name: 'Richmond' },
              { value: crime_list["South Melbourne"], name: 'South Melbourne' },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      };

      option && myChart.setOption(option);
    },

    init_multi_BarChat_job_income(data, html_label, head_label){
      var chartDom = document.getElementById(html_label);
      var myChart = echarts.init(chartDom);
      var option;

      var data_job_list = [] 
      var data_income_list = []
      var city_list = []

      for(var key in data){
          var job_area = data[key]["abs_job"][0]
          var each_job = Math.round(data[key]["abs_job"][1] / job_area)
          var each_income = Math.round(data[key]["abs_job"][2] / job_area)
          data_job_list.push(each_job)
          data_income_list.push(each_income)
          var city = data[key]["city"]
          city_list.push(city)
      }

      option = {
        title: {
          text: head_label  
        },
        legend: {
          data: ["income","job"]
        },
        xAxis: {
          type: 'category',
          data: city_list
        },
        tooltip:{},
        yAxis: {
          type: 'value'
        },
        series: [
          {
            data: data_income_list,
            name: "income",
            type: 'bar',
            showBackground: true,
            backgroundStyle: {
              color: 'rgba(180, 180, 180, 0.2)'
            }
          },
          {
            data: data_job_list,
            name: "job",
            type: 'bar',
            showBackground: true,
            backgroundStyle: {
              color: 'rgba(180, 180, 180, 0.2)'
            }
          }
        ]
      };

      option && myChart.setOption(option);
    },

    //  Daily crime
    init_daily_crime_melbourne(data,html_label){
      var chartDom = document.getElementById(html_label);
      var myChart = echarts.init(chartDom);
      var option;
      var time_list = []
      var crime_list = []
      for (var each_time in data[0]["stream_time"]){
        time_list.push(each_time)
        crime_list.push(data[0]["stream_time"][each_time])
      }
      option = {
        title: {
          text: "Tweets"
        },
        tooltip: {},
        xAxis: {
          type: 'category',
          data: time_list
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            data: crime_list, 
            type: 'line'
          }
        ]
      };

      option && myChart.setOption(option);
    },

    init_Multi_BarChart_diabled_7_30(data, html_label, text_name){
      var myChart = echarts.init(document.getElementById(html_label));

      var disabled_7_list = [] 
      var disabled_30_list = []
      var city_list = [] 

      for(var key in data){
          var seven = data[key]["disabled"]
          var thirty = data[key]["disabled_results_30days"]
          var city = data[key]["city"]
          city_list.push(city)
          disabled_7_list.push(seven)
          disabled_30_list.push(thirty)
      }

      var option = {
        title: {
          text: text_name  
        },
        tooltip: {},
        legend: {
          data: ["7 days", "30 days"]
        },
        xAxis: {
          data: city_list
        },
        yAxis: {},
        series: [
          {
            name: "7 days", 
            type: 'bar',
            data: disabled_7_list
          },
          {
            name: "30 days",
            type: 'bar',
            data: disabled_30_list
          },
        ]
      };
      myChart.setOption(option);
    },
  }
};
</script>
<style scoped>
.bar_chart {
  width: 100%;
  height: 600px;
}
.center {
    height: 2.666667rem;
    width: 100%;
    text-align: center;
}
</style>