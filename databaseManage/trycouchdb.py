import couchdb
import json
import requests


masternode='172.26.134.177'
user='Yingpei'
passeord='030988'
#files = {'file':open('crime_results.json','rb')}
#header = {'Content-Type': 'application/json'}
#data = json.dumps({
#"docs":[
#	{"doc1":"sth","aaaa":"123"},
#	{"doc2":"moremore","bbbb":"456"}
#]})
url = 'http://'+user+':'+passeord+'@'+masternode+':5984/'


#res=requests.post(url=url+'newtest/_bulk_docs',data = '@./crime_results.json'
#,headers=header)
#print(res)
couch = couchdb.Server(url)
try:
	db = couch['rant']
except:
    couch.create('rant')
    db = couch['rant']
    print('no such db, created one')
finally:

#output=couch.replicate(url+"newtest",url+"newrep",continuous=True)
#db = couch['newtest']
#results=db.view('try/city-view',reduce=True,group_level=1)

#outputdict={}
#for row in results:
#	outputdict[row.key]=row.value
#print(outputdict)

#for id in db:
#    print(db[id])
    with open('rant_results.json','r',encoding='utf-8') as f:
        dic = json.load(f)
        #print(dic)
        documents = db.update(dic['docs'])

#output=couch.delete('rant')
#print(output)
