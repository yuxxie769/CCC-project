function (doc) {
  emit(doc.city, [1,doc.properties.erp_2020,doc.properties.pop_density_2020_people_per_km2,doc.properties.pop_density_2020_people_per_km2]);
}