# Hanzhen Yang 1070951, 
# Hanzhong Wang, 1029740,
# Quan Zhou 1065302, 
# Yuhang Xie 1089250, 
# Ze Liu 1073628

import json
import os
import pandas as pd
import urllib.request

Base_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))

# resceive the backend request of state
state = 'nsw'

with open(Base_dir+f'/aurin/{state}_plus.json',encoding='utf-8',) as f2:

    #raw_data 是原始的geo.json
    raw_data = json.load(f2)
    for feature in raw_data['features']:
        del feature['geometry']

    #所有城市遍历完再写进去
    with open(Base_dir+f'/aurin/{state}_analysis.json', 'w') as r:
        print(raw_data)
        json.dump(raw_data, r)

    r.close()

f2.close()
