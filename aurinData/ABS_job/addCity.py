import json
cityCaps = ['A','B','S','M']
cities = ['Adelaide','Brisbane','Sydney','Melbourne']
for index,cap in enumerate(cityCaps):

    filename = cap + '_job.json'
    outputName = cap + '_convert.json'
    with open(filename,'r',encoding='utf-8') as f:
            dic = json.load(f)
            #print(dic)
            for feature in dic['features']:
                feature['city'] = cities[index]
            newdic = dic['features']
            with open(outputName,'w',encoding='utf-8') as f:
                f.write(json.dumps({'docs':newdic}))