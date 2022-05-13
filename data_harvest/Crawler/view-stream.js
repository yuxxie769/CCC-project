function (doc) {
  var date = doc.created_at.slice(0,10)
  emit(date, 1);
}