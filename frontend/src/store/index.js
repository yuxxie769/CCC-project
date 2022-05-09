// Thanks COMP 90024 TEAM 68 Provide template Reference : https://github.com/CCC68/COMP90024_Project2, Hanzhen Yang 1070951, Hanzhong Wang, 1029740, Quan Zhou 1065302, Yuhang Xie 1089250, Ze Liu 1073628
// Modoified By COMP90024 TEAM 45
// Yingpei Ni 1252881
// Yixue Jiang 1023137
// Zirui Shan  1298781
// Jinglin Li 1000797
// Yuxiang Xie 1060196

import { createStore } from 'vuex'

export default createStore({
  state: {
    places: {
      Adelaide: {
        n: 'Adelaide',
        name: 'Adelaide',
        placeField: 'nsw_lga__3',
        coords: { lat: -34.9286212, lng: 138.5999594 },
        zoom: 7, 
        filename: 'Adelaide'
      },
      Brisbane: {
        n: 'Brisbane',
        name: 'Brisbane',
        placeField: 'nsw_lga__3',
        coords: { lat: -27.467778, lng: 153.027778 },
        zoom: 7,
        filename: 'Brisbane'
      },
      Melbourne: {
        n: 'Melbourne',
        name: 'Melbourne',
        placeField: 'nsw_lga__3',
        coords: { lat: -37.8136, lng: 144.963 },
        zoom: 7,
        filename: 'Melbourne'
      },
      Sydney: {
        n: 'Sydney',
        name: 'Sydney',
        placeField: 'NSW_LGA__3',
        coords: { lat: -33.859972, lng: 151.211111 },
        zoom: 7,
        filename: 'Sydney'
      }
    },
    scenarios: ['Crime', 'Income', 'Disabled'], 
    aurins: ['Crime', 'Income', 'Disabled'], 
    silver_map: [
      {
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#f5f5f5"
          }
        ]
      },
      {
        "elementType": "labels.icon",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
      },
      {
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#616161"
          }
        ]
      },
      {
        "elementType": "labels.text.stroke",
        "stylers": [
          {
            "color": "#f5f5f5"
          }
        ]
      },
      {
        "featureType": "administrative.land_parcel",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
      },
      {
        "featureType": "administrative.land_parcel",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#bdbdbd"
          }
        ]
      },
      {
        "featureType": "administrative.neighborhood",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
      },
      {
        "featureType": "poi",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#eeeeee"
          }
        ]
      },
      {
        "featureType": "poi",
        "elementType": "labels.text.fill",
        "stylers": [ 
          {
            "color": "#757575"
          }
        ]
      },
      {
        "featureType": "poi.park",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#e5e5e5"
          }
        ]
      },
      {
        "featureType": "poi.park",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#9e9e9e"
          }
        ]
      },
      {
        "featureType": "road",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#ffffff"
          }
        ]
      },
      {
        "featureType": "road",
        "elementType": "labels",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
      },
      {
        "featureType": "road.arterial",
        "elementType": "labels",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
      },
      {
        "featureType": "road.arterial",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#757575"
          }
        ]
      },
      {
        "featureType": "road.highway",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#dadada"
          }
        ]
      },
      {
        "featureType": "road.highway",
        "elementType": "labels",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
      },
      {
        "featureType": "road.highway",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#616161"
          }
        ]
      },
      {
        "featureType": "road.local",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
      },
      {
        "featureType": "road.local",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#9e9e9e"
          }
        ]
      },
      {
        "featureType": "transit.line",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#e5e5e5"
          }
        ]
      },
      {
        "featureType": "transit.station",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#eeeeee"
          }
        ]
      },
      {
        "featureType": "water",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#c9c9c9"
          }
        ]
      },
      {
        "featureType": "water",
        "elementType": "labels.text",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
      },
      {
        "featureType": "water",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#9e9e9e"
          }
        ]
      }
    ],

  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
