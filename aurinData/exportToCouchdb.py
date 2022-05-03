import couchdb
import json
import requests


masternode='172.26.130.224'
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
foderNames= ['ABS_job','ABS_population','DESE_unemploy','DSS_payment','NDIA_number','SGSEP_rai','UNSW_rental']
dbNames = ['abs_job','abs_population','dese_unemploy','dss_payment','ndia_number','sgsep_rai','unsw_rental']
for index,dbname in enumerate(dbNames):
    try:
        db = couch[dbname]
        couch.delete(dbname)
        couch.create(dbname)
        db = couch[dbname]
    except:
        couch.create(dbname)
        db = couch[dbname]
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
        cityCaps = ['A','B','S','M']
        for cap in cityCaps:
            with open('C:/Users/xt/Documents/GitHub/CCC-project/aurinData/'+foderNames[index]+'/'+cap+'_convert.json','r',encoding='utf-8') as f:
                dic = json.load(f)
                #print(dic)
                documents = db.update(dic['docs'])
    print(dbname +'export finished!')
    #output=couch.delete('rant')
    #print(output)
