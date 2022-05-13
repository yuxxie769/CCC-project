import json
import couchdb
import numpy as np

masternode='172.26.131.249'
user='Yingpei'
passeord='030988'

url = 'http://'+user+':'+passeord+'@'+masternode+':5984/'
couch = couchdb.Server(url)

dbNames = ['abs_job','abs_population','dese_unemploy','dss_payment',
           'ndia_number','sgsep_rai','unsw_rental','crime',
           'disabled','income','newstimeline','rant',
           'crime_results_30days','disabled_results_30days']

final_V_2=[]
suburb=[]
mel={"city":"Melbourne",'cordinate':[[141.1,-38],[147,-38],[147,-37.5],[141.1,-37.5]]}
syd={"city":"Sydney",'cordinate':[[146,-36],[152,-36],[152,-33],[146,-33]]}
ade={"city":"Adelaide",'cordinate':[[138,-35],[138,-38],[141.1,-35],[141.1,-38]]}
bri={"city":"Brisbane",'cordinate':[[148,-30.8],[154,-30.8],[154,-24.5],[148,-24.5]]}
sub_mel={"city":"Melbourne City"}
sub_rich={"city":"Richmond"}
sub_south={"city":"South Melbourne"}

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
            try:
                mid_np = np.array(row.value)
                mid_np_2f = np.round(mid_np, 3)
                list_new = list(mid_np_2f)
                if row.key == "Melbourne":
                    mel[i] = list_new
                elif row.key == "Sydney":
                    syd[i] = list_new
                elif row.key == "Adelaide":
                    ade[i] = list_new
                elif row.key == "Brisbane":
                    bri[i]=list_new
            except:
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
        if row.key == "Melbourne City":
            sub_mel['crime_suburb'] = row.value
        elif row.key == "Richmond":
            sub_rich['crime_suburb']=row.value
        elif row.key == "South Melbourne":
            sub_south['crime_suburb']=row.value

try:
    db = couch['newstimeline']
except:
    couch.create('newstimeline')
    db = couch['newstimeline']
    print('no such db, created one')
finally:
    results = db.view('city/city-view', reduce=True, group_level=2)
    for row in results:
        try:
            mid_np = np.array(row.value)
            mid_np_2f = np.round(mid_np, 3)
            list_new = list(mid_np_2f)
            if row.key[0] == "Melbourne" and str(row.key[1])=="7news":
                mel['news_time_line_7news'] = list_new
            elif row.key[0] == "Melbourne" and str(row.key[1]) == "9news":
                mel['news_time_line_9news'] = list_new
            elif row.key[0] == "Sydney" and str(row.key[1]) == "7news":
                syd['news_time_line_7news'] = list_new
            elif row.key[0] == "Sydney" and str(row.key[1]) == "9news":
                syd['news_time_line_9news'] = list_new
            elif row.key[0] == "Adelaide" and str(row.key[1]) == "7news":
                ade['news_time_line_7news'] = list_new
            elif row.key[0] == "Adelaide" and str(row.key[1]) == "9news":
                ade['news_time_line_9news'] = list_new
            elif row.key[0] == "Brisbane" and str(row.key[1]) == "7news":
                bri['news_time_line_7news'] = list_new
            elif row.key[0] == "Brisbane" and str(row.key[1]) == "9news":
                bri['news_time_line_9news'] = list_new
        except:
            if row.key[0] == "Melbourne" and str(row.key[1])=="7news":
                mel['news_time_line_7news'] = row.value
            elif row.key[0] == "Melbourne" and str(row.key[1]) == "9news":
                mel['news_time_line_9news'] = row.value
            elif row.key[0] == "Sydney" and str(row.key[1]) == "7news":
                syd['news_time_line_7news'] = row.value
            elif row.key[0] == "Sydney" and str(row.key[1]) == "9news":
                syd['news_time_line_9news'] = row.value
            elif row.key[0] == "Adelaide" and str(row.key[1]) == "7news":
                ade['news_time_line_7news'] = row.value
            elif row.key[0] == "Adelaide" and str(row.key[1]) == "9news":
                ade['news_time_line_9news'] = row.value
            elif row.key[0] == "Brisbane" and str(row.key[1]) == "7news":
                bri['news_time_line_7news'] = row.value
            elif row.key[0] == "Brisbane" and str(row.key[1]) == "9news":
                bri['news_time_line_9news'] = row.value


try:
    db = couch['crime']
except:
    couch.create('crime')
    db = couch['crime']
    print('no such db, created one')
finally:
    results = db.view('city/emotion-view', reduce=True, group_level=1)
    for row in results:
        mid_np = np.array(row.value)
        mid_np_2f = np.round(mid_np, 3)
        list_new = list(mid_np_2f)
        if row.key == "Melbourne":
            mel["emotion"] = list_new
        elif row.key == "Sydney":
            syd["emotion"] = list_new
        elif row.key == "Adelaide":
            ade["emotion"] = list_new
        elif row.key == "Brisbane":
            bri["emotion"] = list_new

# stream_time={}
# try:
#     db = couch['stream_crime_mel']
# except:
#     couch.create('stream_crime_mel')
#     db = couch['stream_crime_mel']
#     print('no such db, created one')
# finally:
#     results = db.view('city/city-view', reduce=True, group_level=1)
#     for row in results:
#         stream_time[row.key] = row.value
#     mel["stream_time"]=stream_time

mel["stream_time"]={"2022-05-03": 3, "2022-05-04": 147, "2022-05-05": 79, "2022-05-06": 59, "2022-05-07": 66, "2022-05-08": 38, "2022-05-09": 48, "2022-05-10": 16, "2022-05-11": 27}

final_V_2.append(mel)
final_V_2.append(syd)
final_V_2.append(ade)
final_V_2.append(bri)
suburb.append(sub_mel)
suburb.append(sub_rich)
suburb.append(sub_south)
with open('../temp_data/analysis_data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps({'new_edits': False, 'docs': final_V_2}))
with open('../temp_data/analysis_suburb.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps({'new_edits': False, 'docs': suburb}))

city_list=["Adelaide","Brisbane","Melbourne","Sydney"]
info_list=['abs_job','abs_population', 'dese_unemploy', 'dss_payment', 'ndia_number',
           'sgsep_rai', 'unsw_rental', 'crime', 'disabled', 'income', 'rant', 'crime_results_30days',
           'disabled_results_30days']
with open("../temp_data/analysis_data.json") as f1:
    info = f1.read()
infos=json.loads(info)
for i in range(len(city_list)):
    with open("../temp_data/"+city_list[i]+'.json') as f:
        result=f.read()
    results=json.loads(result)
    for j in range(len(city_list)):
        if infos["docs"][j]["city"] == city_list[i] :
            for k in info_list:
                results["features"][0]["properties"][k] = infos["docs"][j][k]
    with open("../temp_data/"+city_list[i]+'.json', "w") as f2:
        f2.write(json.dumps(results))
    f2.close


