function (doc) {
    if (doc.properties.Renters !== null && doc.properties.Renters !== 0){
        emit(doc.city, doc.properties.Renters);
    }
}