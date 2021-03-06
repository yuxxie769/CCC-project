import couchdb
import json

#This program is for pushing Twitter data into the couchdb
#login couchdb
masternode='172.26.130.224'
user='Yingpei'
passeord='030988'

url = 'http://'+user+':'+passeord+'@'+masternode+':5984/'


couch = couchdb.Server(url)
#Every dataset has an unique database
fileNames= ['crime_suburb.json','disabled_results_30days.json','crime_results_30days.json','NewsTimeLine.json','crime_results.json','disabled_results.json','income_results.json','rant_results.json']
dbNames = ['crime_suburb','disabled_results_30days','crime_results_30days','newstimeline','crime','disabled','income','rant']
#Veiw documents for each databases
design_docs=[{  '_id': '_design/city',
                'views': {
                    'city-view': {
                        'map': 'function(doc){emit(doc.suburb, 1);}',
                        'reduce': '_count'
                    }
                }
            },
            {  '_id': '_design/city',
                'views': {
                    'city-view': {
                        'map': 'function(doc){emit(doc.city, 1);}',
                        'reduce': '_count'
                    }
                }
            },
            {  '_id': '_design/city',
                'views': {
                    'city-view': {
                        'map': 'function(doc){emit(doc.city, 1);}',
                        'reduce': '_count'
                    }
                }
            },
            {  '_id': '_design/city',
                'views': {
                    'city-view': {
                        'map': 'function(doc){if ((parseInt(doc.created_at.slice(6,7))==3 && parseInt(doc.created_at.slice(8,10))>=14) || parseInt(doc.created_at.slice(6,7))>3){emit([doc.city,doc.media], 1);}}',
                        'reduce': '_count'
                    }
                }
            },
            {  '_id': '_design/city',
                'views': {
                    'city-view': {
                        'map': 'function(doc){emit(doc.city, 1);}',
                        'reduce': '_count'
                    },
                    'emotion-view': {
                        'map': 'function(doc){if (doc.emotion.Happy !== 0 || doc.emotion.Angry !== 0 || doc.emotion.Surprise !== 0 || doc.emotion.Sad !== 0 || doc.emotion.Fear !== 0){emit(doc.city, [doc.emotion.Happy,doc.emotion.Angry,doc.emotion.Surprise,doc.emotion.Sad,doc.emotion.Fear]);}}',
                        'reduce': '_sum'
                    }
                }
            },
            {  '_id': '_design/city',
                'views': {
                    'city-view': {
                        'map': 'function(doc){emit(doc.city, 1);}',
                        'reduce': '_count'
                    }
                }
            },
            {  '_id': '_design/city',
                'views': {
                    'city-view': {
                        'map': 'function(doc){emit(doc.city, 1);}',
                        'reduce': '_count'
                    }
                }
            },
            {  '_id': '_design/city',
                'views': {
                    'city-view': {
                        'map': 'function(doc){emit(doc.city, 1);}',
                        'reduce': '_count'
                    }
                }
            },
]
#Create databases and push data and view.
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

                try:
                    resp = db.save(design_docs[index])
                    print(resp)
                except:
                    print('view already exist')
                finally:
                    print(dbname +' export finished!')

