#!/usr/bin/python
import json
import pandas as pd
import re
df = pd.read_csv("../data/vaccine.csv")
ok = open("../data/neighbor-districts.json")
data = json.load(ok)
diff = pd.read_csv("../data/diff.csv")

remove = ['kheri', 'konkan division', 'niwari', 'noklak', 'parbhani', 'pattanamtitta','chengalpattu', 'gaurela pendra marwahi', 'nicobars', 'north and middle andaman', 'saraikela-kharsawan',
'south andaman', 'tenkasi', 'tirupathur', 'yanam','mumbai city'
]

c = {}
for i in range(0,len(diff)):
    c[diff.iloc[i]['json'].replace(' ','',1)] = diff.iloc[i]['district'].replace(' ','',1)

mapp={"bilaspur/Q1478939":"HP_Bilaspur","bilaspur/Q100157":"CT_Bilaspur","aurangabad/Q43086":"BR_Aurangabad","aurangabad/Q592942":"MH_Aurangabad",
                 "balrampur/Q1948380":"UP_Balrampur","balrampur/Q16056268":"CT_Balrampur","bijapur/Q100164":"CT_Bijapur","bijapur_district/Q1727570":"KA_Vijayapura",
                 "hamirpur/Q2019757":"UP_Hamirpur",'hamirpur/Q2086180':"HP_Hamirpur","lakhimpur/Q42743":"AS_Assam","pratapgarh/Q1585433":"RJ_Pratapgarh",
                 "pratapgarh/Q1473962":"UP_Pratapgarh"}


data_re = {}
for i in data.keys():
    z = i.replace('_',' ')
    data_re[z] = []
    for j in data[i]:
        j = j.replace('_',' ')
        data_re[z].append(j)

for i in list(mapp):
    try:
        data_re[mapp[i]] = data_re.pop(i)
    except:
        pass

for i in data_re:
    for j in mapp:
        if j in data_re[i]:
            data_re[i][data_re[i].index(j)] = mapp[j]
        
data_ree = {}
for i in data_re.keys():
    key = re.sub('/Q[0-9]*','',i)
    key = key.replace(' district','')
    data_ree[key] = []
    for j in data_re[i]:
        value = re.sub('/Q[0-9]*','',j)
        value = value.replace(' district','')
        data_ree[key].append(value)

for i in list(c):
    try:
        data_ree[c[i]] = data_ree.pop(i)
    except:
        pass

for i in data_ree:
    for j in c:
        if j in data_ree[i]:
            data_ree[i][data_ree[i].index(j)] = c[j]

for i in list(data_ree):
    if i in remove:
        del data_ree[i]

for i in list(data_ree):
    for j in list(data_ree[i]):
        if j in remove:
            data_ree[i].remove(j)
            
seet = {}
for i in range(0,len(df)):
    seet[df.iloc[i]['District']]=df.iloc[i]['District_Key']

seet['Dadra And Nagar Haveli'] = 'DN_Dadra and Nagar Haveli'
seet['Lahaul And Spiti'] = 'HP_Lahaul and Spiti'


for i in list(seet):
    if i.lower() in list(data_ree):
        try:
            seet[i.title()]
            data_ree[seet[i.title()]] = data_ree.pop(i.lower())
        except:
            pass

for i in data_ree:
    for j in seet:
        if j.lower() in data_ree[i]:
            data_ree[i][data_ree[i].index(j.lower())] = seet[j]
        
final = list(data_ree.keys())
final.sort()
final_data = {}
for i in final:
    c = data_ree[i]
    c.sort()
    final_data[i] = c


a = open('../output/neighbor-districts-modified.json','w')
a.write(json.dumps(final_data))
a.close
