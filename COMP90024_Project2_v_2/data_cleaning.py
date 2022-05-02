# Hanzhen Yang 1070951, 
# Hanzhong Wang, 1029740,
# Quan Zhou 1065302, 
# Yuhang Xie 1089250, 
# Ze Liu 1073628

import json
import os
import pandas as pd



# df = pd.read_csv("aurin/aurin_nsw/income.csv", encoding='utf-8',header=0)
df1 = pd.read_csv("aurin/aurin_nsw/population.csv", encoding='utf-8',header=0)
# df2 = pd.read_csv("aurin/aurin_nsw/obesity.csv", encoding='utf-8',header=0)

print(df1)



# df=df.sort_values(by="lga_code_2016",ascending=True)

# df1=df1.sort_values(by="lga_code16",ascending=True)
# df2 = df2.sort_values(by="lga_code",ascending=True)
#
# search_list = df['lga_code_2016']
# print(search_list)
# df = df1[df1['lga_code16'].isin(search_list)]
# print(df1)
#
# df2 = df2[df2['lga_code'].isin(search_list)]
#
# print(df2)

# for i in range(130):
#     df2.at[i, 'lga_name'] = df2.at[i, 'lga_name'].lower()
#
# df.to_csv("aurin/aurin_nsw/income.csv", encoding='utf-8',index=False)
# df1.to_csv("aurin/aurin_nsw/population.csv", encoding='utf-8',index=False)
# df2.to_csv("aurin/aurin_nsw/obesity.csv", encoding='utf-8',index=False)
