import json
cityCaps = ['A','B','S','M']
cities = ['Adelaide','Brisbane','Sydney','Melbourne']
for index,cap in enumerate(cityCaps):

    filename = cap + '_unemp.json'
    outputName = cap + '_convert.json'
    with open(filename,'r',encoding='utf-8') as f:
            dic = json.load(f)
            #print(dic)
            for feature in dic['features']:
                feature['city'] = cities[index]
                if feature['properties']['dec_10'] != None:
                    feature['properties']['dec_10'] = float(feature['properties']['dec_10'])
            newdic = dic['features']
            with open(outputName,'w',encoding='utf-8') as f:
                f.write(json.dumps({'docs':newdic}))