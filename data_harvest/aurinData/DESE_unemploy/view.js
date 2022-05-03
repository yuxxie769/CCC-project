function (doc) {
  if (doc.properties.dec_10 !== null){
      emit(doc.city, [1,doc.properties.dec_10]);
  }
}