# flask的配置
import json
import couchdb

masternode='172.26.130.224'
user='Yingpei'
passeord='030988'

url = 'http://'+user+':'+passeord+'@'+masternode+':5984/'
couch = couchdb.Server(url)

#filename = "vic_plus.json"
dbNames = ['abs_job','abs_population','dese_unemploy','dss_payment','ndia_number','sgsep_rai','unsw_rental','crime',
           'disabled','income','news_time_line','rant','crime_results_30days','disabled_results_30days']

#res=requests.post(url=url+'newtest/_bulk_docs',data = '@./crime_results.json'
#,headers=header)
#print(res)

final_out=[]
sub_out=[]
mel={"city":"Melbourne"}
syd={"city":"Sydney"}
ade={"city":"Adelaide"}
bri={"city":"Brisbane"}
sub_mel={"city":"Melbourne City"}
sub_rich={"city":"Richmond"}
sub_south={"city":"South Melbourne"}

# dbs = couch['crime_sub']
# results=dbs.view('city/city-view',reduce=True,group_level=1)
# print(results)

for i in dbNames:
    try:
        db = couch[i]
    except:
        couch.create(i)
        db = couch[i]
        print('no such db, created one')
    finally:
        results=db.view('city/city-view',reduce=True,group_level=1)
        print(results)
        for row in results:
            #print(row.key)
            if row.key == "Melbourne":
                mel[i] = row.value
            elif row.key == "Sydney":
                syd[i] = row.value
            elif row.key == "Adelaide":
                ade[i] = row.value
            elif row.key == "Brisbane":
                bri[i]=row.value

try:
    db = couch['crime_suburb']
except:
    couch.create('crime_suburb')
    db = couch['crime_suburb']
    print('no such db, created one')
finally:
    results = db.view('city/city-view', reduce=True, group_level=1)
    for row in results:
        print(row.key)
        print(row.value)
        if row.key[0] == "Melbourne City":
            sub_mel['crime_suburb'] = row.value
        elif row.key[0] == "Richmond":
            sub_rich['crime_suburb']=row.value
        elif row.key[0] == "South Melbourne":
            sub_south['crime_suburb']=row.value

final_out.append(mel)
final_out.append(syd)
final_out.append(ade)
final_out.append(bri)
sub_out.append(sub_mel)
sub_out.append(sub_rich)
sub_out.append(sub_south)
print(final_out)
print(sub_out)
with open('final.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps({'new_edits': False, 'docs': final_out}))
with open('sub.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps({'new_edits': False, 'docs': sub_out}))


        # with open(i + '.json', 'w', encoding='utf-8') as f:
        #     f.write(json.dumps({'new_edits': False, 'docs': outputdict}))
#
#         print(outputdict)
# try:
#     db = couch["crime"]
# except:
#     couch.create("crime")
#     db = couch["crime"]
#     print('no such db, created one')
# finally:
#     results=db.view('city/city-view',reduce=True,group_level=1)
#     outputdict={}
#     for row in results:
#         outputdict[row.key]=row.value
#     with open("crime" + '.json', 'w', encoding='utf-8') as f:
#         f.write(json.dumps({'new_edits': False, 'docs': outputdict}))
# try:
#     return json.dumps(outputdict)
#     #return outputdict
# except Exception as e:
#     return jsonify({"code": "Error", "message": "{}".format(e)})
