function (doc) {
  emit(doc.city, doc.properties.number_participants);
}