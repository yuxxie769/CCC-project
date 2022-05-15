import couchdb
import json
import requests

#This program is for pushing aurin data into the couchdb
#login couchdb
masternode='172.26.130.224'
user='Yingpei'
passeord='030988'

url = 'http://'+user+':'+passeord+'@'+masternode+':5984/'
couch = couchdb.Server(url)

#every dataset has an unique database
foderNames= ['ABS_job','ABS_population','DESE_unemploy','DSS_payment','NDIA_number','SGSEP_rai','UNSW_rental']
dbNames = ['abs_job','abs_population','dese_unemploy','dss_payment','ndia_number','sgsep_rai','unsw_rental']
#veiw documents for each databases
design_docs = [
    {  '_id': '_design/city',
                        'views': {
                            'city-view': {
                                'map': 'function(doc){emit(doc.city, [1,doc.properties.number_of_jobs_000_persons_2018_19,doc.properties.median_employment_income_per_job_persons_2018_19]);}',
                                'reduce': '_sum'
                            }
                        }
    },
    {  '_id': '_design/city',
                        'views': {
                            'city-view': {
                                'map': 'function(doc){emit(doc.city, [1,doc.properties.erp_2020,doc.properties.pop_density_2020_people_per_km2]);}',
                                'reduce': '_sum'
                            }
                        }
    },
    {  '_id': '_design/city',
                        'views': {
                            'city-view': {
                                'map': 'function(doc){if (doc.properties.dec_10 !== null){emit(doc.city, [1,doc.properties.dec_10]);}}',
                                'reduce': '_sum'
                            }
                        }
    },
    {  '_id': '_design/city',
                        'views': {
                            'city-view': {
                                'map': 'function(doc){emit(doc.city, doc.properties.disability_support_pension);}',
                                'reduce': '_sum'
                            }
                        }
    },
    {  '_id': '_design/city',
                        'views': {
                            'city-view': {
                                'map': 'function(doc){emit(doc.city, doc.properties.number_participants);}',
                                'reduce': '_sum'
                            }
                        }
    },
    {  '_id': '_design/city',
                        'views': {
                            'city-view': {
                                'map': 'function(doc){if (doc.properties.rai_cityadjusted_total_2020_q1 !== null && doc.properties.rai_cityadjusted_total_2020_q2 !== null && doc.properties.rai_cityadjusted_total_2020_q3 !== null && doc.properties.rai_cityadjusted_total_2020_q4 !== null){emit(doc.city, [1,doc.properties.rai_cityadjusted_total_2020_q1,doc.properties.rai_cityadjusted_total_2020_q2,doc.properties.rai_cityadjusted_total_2020_q3,doc.properties.rai_cityadjusted_total_2020_q4]);}}',
                                'reduce': '_sum'
                            }
                        }
    },
    {  '_id': '_design/city',
                        'views': {
                            'city-view': {
                                'map': 'function(doc){if (doc.properties.Renters !== null && doc.properties.Renters !== 0){emit(doc.city, doc.properties.Renters);}}',
                                'reduce': '_sum'
                            }
                        }
    }
]
#create databases and push data and view.
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
        cityCaps = ['A','B','S','M']
        for cap in cityCaps:
            with open(foderNames[index]+'/'+cap+'_convert.json','r',encoding='utf-8') as f:
                dic = json.load(f)
                #print(dic)
                documents = db.update(dic['docs'])
        resp = db.save(design_docs[index])
        print(resp)        
    print(dbname +'export finished!')
