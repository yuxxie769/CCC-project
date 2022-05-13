import couchdb
import json


masternode='172.26.130.224'
user='Yingpei'
passeord='030988'

url = 'http://'+user+':'+passeord+'@'+masternode+':5984/'


#res=requests.post(url=url+'newtest/_bulk_docs',data = '@./crime_results.json'
#,headers=header)
#print(res)
couch = couchdb.Server(url)
fileNames= ['crime_suburb.json']
dbNames = ['crime_suburb']
design_doc={  '_id': '_design/city',
            'views': {
                'city-view': {
                    'map': 'function(doc){emit(doc.suburb, 1);}',
                    'reduce': '_count'
                }
            }
    }
for index,dbname in enumerate(dbNames):
    try:
        db = couch[dbname]
    except:
        couch.create(dbname)
        db = couch[dbname]
        print('no such db, created one')
    finally:
            with open(fileNames[index],'r',encoding='utf-8') as f:
                dic = json.load(f)
                for doc in dic['docs']:
                    doc['_id'] = str(doc['_id'])
                #print(dic)
                documents = db.update(dic['docs'])
                resp = db.save(design_doc)
                print(resp)
                print(dbname +' export finished!')

