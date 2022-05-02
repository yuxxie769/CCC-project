import couchdb
import json

couch = couchdb.Server('http://adm1n_c0uchd6:_gr0up68H1_@localhost:5984')

traffic_vic_db = couch.create('traffic_vic_db')

json_file = "/home/ubuntu/COMP90024_Project2/crawler/traffic_vic.json"

with open(json_file) as f:
    line = f.readline()
    while line != "":
        try:
            db_entry = json.loads(line)
            traffic_vic_db.save(db_entry)
        except Exception as e:
            print(e)
            line = f.readline()
        line = f.readline()
            
docs = [{
    "_id": "_design/traffic_location_count",
    "language" : "javascript",
    "views": {
        "all": {
            "map": "function(doc){ \
                emit(doc.user.location, 1) }",
            "reduce": "function(keys, values, rereduce){ return sum(values); }"
        }
    }
}]

resultList = traffic_vic_db.update(docs)
traffic_vic_db.resource.put("_security", {"members":{"roles":[]},"admins":{"roles":[]}})
