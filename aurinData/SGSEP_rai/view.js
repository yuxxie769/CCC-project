
function (doc) {
  if (doc.properties.rai_cityadjusted_total_2020_q1 !== null && doc.properties.rai_cityadjusted_total_2020_q2 !== null && doc.properties.rai_cityadjusted_total_2020_q3 !== null && doc.properties.rai_cityadjusted_total_2020_q4 !== null){
      emit(doc.city, [1,doc.properties.rai_cityadjusted_total_2020_q1,doc.properties.rai_cityadjusted_total_2020_q2,doc.properties.rai_cityadjusted_total_2020_q3,doc.properties.rai_cityadjusted_total_2020_q4]);
  }
}