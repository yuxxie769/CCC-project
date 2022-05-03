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
fileNames= ['disabled_results_30days.json','crime_results_30days.json','NewsTimeLine.json','crime_suburb.json']
dbNames = ['disabled_results_30days','crime_results_30days','newstimeline','crime_suburb']
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
                print(dbname +' export finished!')

