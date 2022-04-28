import json
cityCaps = ['A','B','S','M']
cities = ['Adelaide','Brisbane','Sydney','Melbourne']
for index,cap in enumerate(cityCaps):

    filename = cap + '_Rai.json'
    outputName = cap + '_Rai_convert.json'
    with open(filename,'r',encoding='utf-8') as f:
            dic = json.load(f)
            #print(dic)
            for feature in dic['features']:
                feature['city'] = cities[index]
                feature.pop('geometry')
            newdic = dic['features']
            with open(outputName,'w',encoding='utf-8') as f:
                f.write(json.dumps({'docs':newdic}))