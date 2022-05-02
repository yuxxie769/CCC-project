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
export default {
  setup() {},
  data() {
    return {
      currentPlace: null,
      currentScenario: null,
      currentAurin: null,
      max: -Infinity,
      min: Infinity,
    };
  },
  computed: {
    legendTitle() {
      console.log("currentAurin",this.currentAurin);
      if (this.currentAurin === "Income") {
        return "Median Income ($)";
      } else if (this.currentAurin === "Obesity") {
        return "Obesity Rate (%)";
      } else {
        return this.currentAurin;
      }
    },
  },
  beforeMount() {
    this.initData();

    const loader = new Loader({
      apiKey: process.env.VUE_APP_GOOGLE_MAP_KEY,
      version: "weekly",
    });

    loader.load().then(() => {
      console.log("key", process.env.VUE_APP_GOOGLE_MAP_KEY);
      let google = window.google;
      console.log('google',google);
      let map = new google.maps.Map(document.getElementById("map"), {
        // Map Options like 'center' & 'zoom'
        styles: this.$store.state.silver_map,
        streetViewControl: false,
      });

      this.map = window.map = map;

      this.switchPlace("vic");
      this.setColor();

      this.infowindow = new window.google.maps.InfoWindow();

      map.data.addListener("click", (event) => {
        // console.log(event.feature);
        this.createInfoWindow(map, event);
      });

      map.data.addListener("mouseover", (event) => {
        map.data.revertStyle();
        map.data.overrideStyle(event.feature, {
          strokeColor: "grey",
          strokeWeight: 4,
        });
      });
      map.data.addListener("mouseout", () => {
        map.data.revertStyle();
      });
    });
  },
  mounted() {
    this.currentScenario = document.getElementById("sel_sce").value;
    // console.log("this.currentScenario",this.currentScenario)
    this.currentAurin = document.getElementById("sel_aur").value;
    // console.log("this.currentAurin",this.currentAurin)
    this.changeLegend();
  },
  methods: {
    initData() {
      this.places = this.$store.state.places;
      this.scenarios = this.$store.state.scenarios;
      this.aurins = this.$store.state.aurins;
      this.google = window.google;
    },
    clearMap() {
      let map = this.map;
      this.infowindow?.close();
      map.data.forEach(function (feature) {
        map.data.remove(feature);
      });
    },
    
    switchPlace(event) {
      this.clearMap();
      let n = event.target?.value || event;
      let { coords, zoom, filename } = this.places[n];
      let map = this.map;
      let url = "http://127.0.0.1:5000/" + filename;      //process.env.VUE_APP_BACKEND_BASE_URL + filename;
      this.currentPlace = this.places[n];

      // console.log(coords);
      map.setZoom(zoom);
      map.setCenter(coords);
      map.data.loadGeoJson(url);
    },

    switchScenario(e) {
      this.currentScenario = e.target.value;
      this.infowindow.close();
    },

    switchAurin(e) {
      this.currentAurin = e.target.value;
      this.infowindow.close();
      this.setColor();
    },

    createInfoWindow(map, event) {
      let name = event.feature.getProperty(this.currentPlace.placeField);

      let bitcoin_tweets_count = event.feature.getProperty(
        "bitcoin_tweets_count"
      );
      let traffic_tweets_count = event.feature.getProperty(
        "traffic_tweets_count"
      );
      let exercise_tweets_count = event.feature.getProperty(
        "exercise_tweets_count"
      );

      let income_2014 = event.feature.getProperty("income_2014");
      let obesity = event.feature.getProperty("obesity_rate");
      let population = event.feature.getProperty("population");

      let obesityPieChart = `<div id="obesityPieChart" style="height:240px;width:300px;"></div>`;
      let bitcoin = `<div>Tweets related to Bitcoin: ${bitcoin_tweets_count}</div>`;
      let traffic = `<div>Tweets related to traffic: ${traffic_tweets_count}</div>`;
      let exrecise = `<div>Tweets related to exercise: ${exercise_tweets_count}</div>`;
      let income = `<div>Income: ${income_2014}</div>`;
      let contentString = `<div id="content">
            <div id="siteNotice">${this.currentPlace.name}</div>
            <h5 id="firstHeading" class="firstHeading">${name}</h5>
            <div id="bodyContent">
              ${this.currentScenario === "Bitcoin" ? bitcoin : ""}
              ${this.currentScenario === "Traffic" ? traffic : ""}
              ${this.currentScenario === "Exercise" ? exrecise : ""}
              Population: ${population}
              ${this.currentAurin === "Income" ? income : ""}
              ${
                obesity && this.currentAurin === "Obesity"
                  ? obesityPieChart
                  : ""
              }
            </div>
           </div>`;

      // Center info window on selected zip code area
      // Find center of zip code area by converting
      // the corresponding Polygon object to a
      // LatLngBounds object which has the getCenter function
      var bounds = new window.google.maps.LatLngBounds();
      var geometry = event.feature.getGeometry();

      geometry.forEachLatLng(function (point) {
        console.log("bounds",bounds)
        bounds.extend({
          lat: point.lat(),
          lng: point.lng(),
        });
      });
      var center = bounds.getCenter();

      // Create invisible marker for info window
      var marker = new window.google.maps.Marker({
        position: center,
        map: map,
        visible: false,
      });
      // Create info window
      this.infowindow.setContent(contentString);
      this.infowindow.open(map, marker);

      // import * as echarts from 'echarts';

      if (obesity && this.currentAurin === "Obesity") {
        setTimeout(() => {
          var chartDom = document.getElementById("obesityPieChart");
          var myChart = echarts.init(chartDom);
          var option;

          option = {
            tooltip: {
              trigger: "item",
            },
            legend: {
              top: "0%",
              left: "center",
            },
            series: [
              {
                name: "Obesity Rate",
                type: "pie",
                radius: ["40%", "70%"],
                avoidLabelOverlap: false,
                itemStyle: {
                  borderRadius: 10,
                  borderColor: "#fff",
                  borderWidth: 2,
                },
                label: {
                  show: true,
                  // position: 'center',
                  formatter: "{d}%",
                },
                emphasis: {
                  // label: {
                  //   show: true,
                  //   fontSize: "40",
                  //   fontWeight: "bold",
                  // },
                },
                labelLine: {
                  show: true,
                },
                data: [
                  { value: obesity, name: "Obesity" },
                  { value: population - obesity, name: "Other" },
                ],
              },
            ],
          };

          option && myChart.setOption(option);
        }, 0);
      }
    },
    getIncomeFill(income) {
      let colors = this.$store.state.income_color;
      if (income === undefined) {
        return "grey";
      }
      if (income <= 30000) {
        return colors[0];
      } else if (income >= 60000) {
        return colors[colors.length - 1];
      } else {
        return colors[(((income - 30000) / 2500) >> 0) + 1];
      }
    },
    getPopulationFill(population) {
      if (population === undefined) {
        return "grey";
      }
      let L =
        population > 360000 ? "50%" : 90 - ((population / 36000) >> 0) * 4;
      return `hsl(40deg 100% ${L}%)`;
    },
    getObesityFill(obesity, population) {
      // console.log(obesity);
      if (obesity === undefined || obesity > population) {
        return "grey";
      }
      let ratio = obesity / population;
      let L = ratio > 0.35 ? 0.35 : 80 - (((ratio - 0.1) / 0.025) >> 0) * 4;
      return `hsl(210deg 60% ${L}%)`;
    },
    setColor() {
      this.changeLegend();
      this.map.data.setStyle((feature) => {
        console.log("feature",feature)
        let color;
        let population = feature.getProperty("population");
        let income = feature.getProperty("income_2014");
        let obesity = feature.getProperty("obesity_rate");
        if (this.currentAurin === "Population") {
          color = this.getPopulationFill(population);
        } else if (this.currentAurin === "Income") {
          color = this.getIncomeFill(income);
        } else if (this.currentAurin === "Obesity") {
          color = this.getObesityFill(obesity, population);
        }
        return {
          fillColor: color,
          fillOpacity: 0.7,
          strokeColor: color,
          strokeWeight: 1,
        };
      });
    },
    changeLegend() {
      let dom = document.getElementById("legendColors");
      dom.innerHTML = "";
      // let height = dom.offsetHeight;
      let colors;
      if (this.currentAurin === "Income") {
        colors = this.$store.state.income_color;
        for (let i = 0; i < colors.length; i++) {
          let value;
          if (i === 0) {
            value = "> 60000";
          } else if (i === colors.length - 1) {
            value = "< 30000";
          } else {
            value = 60000 - i * 2500;
          }
          this.createColor(`${colors[colors.length - i - 1]}b3`, value);
        }
      } else if (this.currentAurin === "Population") {
        for (let i = 0; i < 10; i++) {
          let value = 360000 - i * 36000;
          let L = 90 - (value / 36000) * 4;
          this.createColor(`hsl(40deg 100% ${L}% / 70%)`, value, "#666");
        }
      } else if (this.currentAurin === "Obesity") {
        for (let i = 0; i < 10; i++) {
          let value = 0.35 - i * 0.025;
          let L = 80 - (value / 0.025) * 4;
          this.createColor(`hsl(210deg 60% ${L}% / 70%)`, Math.round(value * 100), "#fff");
        }
      }
    },
    createColor(background, value, textColor) {
      let dom = document.getElementById("legendColors");
      let color = document.createElement("div");
      color.className = "subColor";
      color.style.background = background;
      let textStyle = `style="color: ${textColor}; text-shadow:none"`
      color.innerHTML = 
        `<span class="value"${textColor ? textStyle : ""}>${value}<span>`;
      dom.appendChild(color);
    },
  },
};
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