<!-- Thanks COMP 90024 TEAM 68 Provide template Reference : https://github.com/CCC68/COMP90024_Project2, Hanzhen Yang 1070951, Hanzhong Wang, 1029740, Quan Zhou 1065302, Yuhang Xie 1089250, Ze Liu 1073628
Modoified By COMP90024 TEAM 45
Yingpei Ni 1252881
Yixue Jiang 1023137
Zirui Shan  1298781
Jinglin Li 1000797
Yuxiang Xie 1060196 -->
<template>
  <div class="datamap view">
    <div id="map"></div>
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
  },
  beforeMount() {
    this.initData();

    const loader = new Loader({
      apiKey: process.env.VUE_APP_GOOGLE_MAP_KEY,
      version: "weekly",
    });

    loader.load().then(() => {
      let google = window.google;
      let map = new google.maps.Map(document.getElementById("map"), {
        styles: this.$store.state.silver_map,
        streetViewControl: false,
      });

      this.map = window.map = map;

      this.switchPlace("Adelaide");
      this.setColor();

      this.infowindow = new window.google.maps.InfoWindow();

      map.data.addListener("click", (event) => {
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
    this.currentAurin = document.getElementById("sel_aur").value;
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
      let url = "http://127.0.0.1:5000/map/" + filename; 
      this.currentPlace = this.places[n];

      map.setZoom(zoom);
      map.setCenter(coords);
      map.data.loadGeoJson(url);
      console.log("url",url)
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
      // let name = event.feature.getProperty(this.currentPlace.placeField);

      let income_twitter = event.feature.getProperty("income");
      let crime_twitter = event.feature.getProperty("crime");
      let disabled_twitter = event.feature.getProperty("disabled");
      let income_aurine = event.feature.getProperty("abs_job")[2];
      let crime_aurine = event.feature.getProperty("dese_unemploy")[1];
      let disabled_aurine = event.feature.getProperty("ndia_number");

      let income_twitter_html = `<h6> Income twitter: ${income_twitter}</h6>`;
      let crime_twitter_html = `<h6> Crime twitter: ${crime_twitter}</h6>`;
      let disabled_twitter_html = `<h6> Disabled twitter: ${disabled_twitter}</h6>`;
      let income_aurine_html = `<h6> Income_aurine: ${income_aurine}</h6>`;
      let crime_aurine_html = `<h6> Crime aurine: ${crime_aurine}</h6>`;
      let disabled_aurine_html = `<h6> Disabled aurine: ${disabled_aurine}</h6>`;
      let pic_adelaide = '<img src="https://res.klook.com/image/upload/Mobile/City/zb5xnlar4ifecn8cp4h2.jpg" width="350" height="250">';
      let pic_melbourne = '<img src="https://cdn.britannica.com/64/190464-050-B74E1FD9/view-central-business-district-Melbourne-train-station.jpg" width="350" height="250">';
      let pic_sydney = '<img src="https://cms.finnair.com/resource/blob/673152/3523a759b61b788b834fe56aa57fa255/sydney-main-data.jpg" width="350" height="250">';
      let pic_brisbane = '<img src="https://res.cloudinary.com/enchanting/w_1600,h_700,c_fill/artemis-mdm/b03d9fa9-0f08-4d56-bfd1-94c3746decaf.jpg" width="350" height="250">';
      let contentString = `<div id="content">
            <h5 id="firstHeading" class="firstHeading">${this.currentPlace.name}</h5>
            <div id="bodyContent">
              ${this.currentScenario === "Income" ? income_twitter_html : ""}
              ${this.currentScenario === "Crime" ? crime_twitter_html : ""}
              ${this.currentScenario === "Disabled" ? disabled_twitter_html : ""}
              ${this.currentAurin === "Income" ? income_aurine_html : ""}
              ${this.currentAurin === "Disabled" ? disabled_aurine_html : ""}
              ${this.currentAurin === "Crime" ? crime_aurine_html : ""}
            </div>
            <div>
              ${this.currentPlace.name === "Adelaide" ? pic_adelaide : ""}
              ${this.currentPlace.name === "Melbourne" ? pic_melbourne : ""}
              ${this.currentPlace.name === "Sydney" ? pic_sydney : ""}
              ${this.currentPlace.name === "Brisbane" ? pic_brisbane : ""}
            </div>
           </div>`;

      // Center info window on selected zip code area
      // Find center of zip code area by converting
      // the corresponding Polygon object to a
      // LatLngBounds object which has the getCenter function
      var bounds = new window.google.maps.LatLngBounds();
      var geometry = event.feature.getGeometry();

      geometry.forEachLatLng(function (point) {
        bounds.extend({
          lat: point.lat(),
          lng: point.lng(),
        });
      });
      
      var center = bounds.getCenter();

      var marker = new window.google.maps.Marker({
        position: center,
        map: map,
        visible: false,
      });
      // Create info window
      this.infowindow.setContent(contentString);
      this.infowindow.open(map, marker);
    },
    
    getIncomeFill(income) {
      if (income === "Income") {
        return "grey";
      }
      let L =
        income > 360000 ? "50%" : 90 - ((income / 36000) >> 0) * 4;
      return `hsl(40deg 100% ${L}%)`;
    },
    getCrimeFill(crime) {
      if (crime === "Crime") {
        return "grey";
      }
      let L =
        crime > 360000 ? "50%" : 90 - ((crime / 36000) >> 0) * 4;
      return `hsl(40deg 100% ${L}%)`;
    },
    getDisabledFill(disabled) {
      if (disabled === "Disabled") {
        return "grey";
      }
      let L =
        disabled > 360000 ? "50%" : 90 - ((disabled / 36000) >> 0) * 4;
      return `hsl(40deg 100% ${L}%)`;
    },
    setColor() {
      this.map.data.setStyle((feature) => {
        let color;
        let crime = feature.getProperty("ndia_number");
        let income = feature.getProperty("abs_job")[2];
        let disabled = feature.getProperty("dese_unemploy")[1];
        if (this.currentAurin === "Crime") {
          color = this.getCrimeFill(crime);
        } else if (this.currentAurin === "Income") {
          color = this.getIncomeFill(income);
        } else if (this.currentAurin === "Disabled") {
          color = this.getDisabledFill(disabled);
        }
        return {
          fillColor: color,
          fillOpacity: 0.7,
          strokeColor: color,
          strokeWeight: 1,
        };
      });
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