import couchdb
import json

couch = couchdb.Server('http://adm1n_c0uchd6:_gr0up68H1_@localhost:5984')

bitcoin_qld_db = couch.create('bitcoin_qld_db')

json_file = "/home/ubuntu/COMP90024_Project2/crawler/bitcoin_qld.json"

with open(json_file) as f:
    line = f.readline()
    while line != "":
        try:
            db_entry = json.loads(line)
            bitcoin_qld_db.save(db_entry)
        except Exception as e:
            print(e)
            line = f.readline()
        line = f.readline()
            
docs = [{
    "_id": "_design/bitcoin_location_count",
    "language" : "javascript",
    "views": {
        "all": {
            "map": "function(doc){ \
                emit(doc.user.location, 1) }",
            "reduce": "function(keys, values, rereduce){ return sum(values); }"
        }
    }
}]

resultList = bitcoin_qld_db.update(docs)
bitcoin_qld_db.resource.put("_security", {"members":{"roles":[]},"admins":{"roles":[]}})
