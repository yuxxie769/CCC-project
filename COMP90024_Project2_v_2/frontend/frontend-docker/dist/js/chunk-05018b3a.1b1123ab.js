(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-05018b3a"],{"0c67":function(t,a,e){"use strict";e("ae91")},1148:function(t,a,e){"use strict";var i=e("a691"),n=e("1d80");t.exports=function(t){var a=String(n(this)),e="",o=i(t);if(o<0||o==1/0)throw RangeError("Wrong number of repetitions");for(;o>0;(o>>>=1)&&(a+=a))1&o&&(e+=a);return e}},"408a":function(t,a,e){var i=e("c6b6");t.exports=function(t){if("number"!=typeof t&&"Number"!=i(t))throw TypeError("Incorrect invocation");return+t}},"9aef":function(t,a,e){"use strict";e.r(a);var i=e("7a23"),n=Object(i["C"])("data-v-6e5850b1");Object(i["s"])("data-v-6e5850b1");var o={class:"views"},r=Object(i["e"])('<div class="container" data-v-6e5850b1><h2 class="mt-5" data-v-6e5850b1>Population</h2><div id="vic_population_bar" class="bar_chart mt-5" data-v-6e5850b1></div><div id="nsw_population_bar" class="bar_chart mt-3" data-v-6e5850b1></div><hr data-v-6e5850b1><h2 class="mt-5" data-v-6e5850b1>Income</h2><div id="vic_income_bar" class="bar_chart mt-5" data-v-6e5850b1></div><div id="nsw_income_bar" class="bar_chart mt-3" data-v-6e5850b1></div><hr data-v-6e5850b1><h2 class="mt-5" data-v-6e5850b1>Obesity Rate</h2><div id="vic_obesity_bar" class="bar_chart mt-5" data-v-6e5850b1></div><div id="nsw_obesity_bar" class="bar_chart mt-3" data-v-6e5850b1></div></div>',1);Object(i["q"])();var c=n((function(t,a,e,n,c,s){return Object(i["p"])(),Object(i["d"])("div",o,[r])})),s=(e("d3b7"),e("99af"),e("b0c0"),e("159b"),e("b680"),e("313e")),u={setup:function(){},data:function(){return{vic:null,nsw:null,aurin:{population:"population",income:"income_2014",obesity:"obesity_rate"}}},watch:{},beforeMount:function(){},mounted:function(){this.fetchData("vic"),this.fetchData("nsw")},methods:{fetchData:function(t){var a=this;fetch("".concat("http://172.26.132.191:5000/","analysis/").concat(t)).then((function(t){return t.json()})).then((function(e){a[t]=e.features,a.initBarChart(t,"population"),a.initBarChart(t,"income"),a.initBarChart(t,"obesity")}))},initBarChart:function(t,a){var e=this.$store.state.places[t].name,i=[],n=[],o=this.aurin[a];this[t].forEach((function(e){var r=e.properties[o];if(!r)return!0;var c=e.properties["".concat(t,"_lga__3")];i.push(c),n.push("obesity"!==a?r:(r/e.properties.population*100).toFixed(4))})),console.log("".concat(t,"_").concat(a,"_bar"));var r,c=document.getElementById("".concat(t,"_").concat(a,"_bar")),u=s["a"](c),d={income:"The Median Income of ".concat(e," Residents in 2014"),population:"The Population in Each Local Government Area of ".concat(e),obesity:"The Obesity Rate of People over 18 years old in ".concat(e)},l={income:"#5470c6",population:"#ffc107",obesity:"#20c997"};r={title:{text:d[a],left:"center"},color:l[a],tooltip:{trigger:"axis",axisPointer:{type:"shadow"},formatter:function(t){var e=t[0],i={income:"".concat(e.name,"<br/>AUD $").concat(e.value),population:"".concat(e.name,"<br/>").concat(e.value),obesity:"".concat(e.name,"<br/>").concat(e.value,"%")};return i[a]}},grid:{top:"10%",bottom:"30%"},xAxis:{type:"category",data:i,axisLabel:{interval:0,rotate:45}},yAxis:{type:"value"},series:[{data:n,type:"bar",showBackground:!1,backgroundStyle:{color:"rgba(180, 180, 180, 0.2)"}}],dataZoom:[{show:!0,realtime:!0,start:0,end:30}]},r&&u.setOption(r)},initBoxplot:function(){}}};e("0c67");u.render=c,u.__scopeId="data-v-6e5850b1";a["default"]=u},ae91:function(t,a,e){},b680:function(t,a,e){"use strict";var i=e("23e7"),n=e("a691"),o=e("408a"),r=e("1148"),c=e("d039"),s=1..toFixed,u=Math.floor,d=function(t,a,e){return 0===a?e:a%2===1?d(t,a-1,e*t):d(t*t,a/2,e)},l=function(t){var a=0,e=t;while(e>=4096)a+=12,e/=4096;while(e>=2)a+=1,e/=2;return a},b=function(t,a,e){var i=-1,n=e;while(++i<6)n+=a*t[i],t[i]=n%1e7,n=u(n/1e7)},v=function(t,a){var e=6,i=0;while(--e>=0)i+=t[e],t[e]=u(i/a),i=i%a*1e7},h=function(t){var a=6,e="";while(--a>=0)if(""!==e||0===a||0!==t[a]){var i=String(t[a]);e=""===e?i:e+r.call("0",7-i.length)+i}return e},f=s&&("0.000"!==8e-5.toFixed(3)||"1"!==.9.toFixed(0)||"1.25"!==1.255.toFixed(2)||"1000000000000000128"!==(0xde0b6b3a7640080).toFixed(0))||!c((function(){s.call({})}));i({target:"Number",proto:!0,forced:f},{toFixed:function(t){var a,e,i,c,s=o(this),u=n(t),f=[0,0,0,0,0,0],p="",m="0";if(u<0||u>20)throw RangeError("Incorrect fraction digits");if(s!=s)return"NaN";if(s<=-1e21||s>=1e21)return String(s);if(s<0&&(p="-",s=-s),s>1e-21)if(a=l(s*d(2,69,1))-69,e=a<0?s*d(2,-a,1):s/d(2,a,1),e*=4503599627370496,a=52-a,a>0){b(f,0,e),i=u;while(i>=7)b(f,1e7,0),i-=7;b(f,d(10,i,1),0),i=a-1;while(i>=23)v(f,1<<23),i-=23;v(f,1<<i),b(f,1,1),v(f,2),m=h(f)}else b(f,0,e),b(f,1<<-a,0),m=h(f)+r.call("0",u);return u>0?(c=m.length,m=p+(c<=u?"0."+r.call("0",u-c)+m:m.slice(0,c-u)+"."+m.slice(c-u))):m=p+m,m}})}}]);
//# sourceMappingURL=chunk-05018b3a.1b1123ab.js.map