import json
key_words = ['crime','criminal','robbery','theft','murder','illegal','stab','drug','victims','victim','injured','shooting','shootings','police','died','dead','casualty','flames','fire']

with open('suburb_dataset.json',encoding='utf-8') as f:
    dataDic = json.load(f)
    dataDicList = dataDic['docs']
results     = []
for data in dataDicList:
    for keyword in key_words:
        if (data['text'].lower().find(keyword) != -1):
                data['created_at'] = data['created_at'][-4:]
                results.append(data)
                break

print('total qualified data '+str(len(results)))
with open('crime_suburb.json','w',encoding='utf-8') as f:
    f.write(json.dumps({'docs':results}))
    print('crime_suburb.json is finished')
