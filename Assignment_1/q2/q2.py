import pandas as pd
import json

file1 = open('../output/neighbor-districts-modified.json')
data = json.load(file1)

k =[]
for i in data.keys():
    for j in data[i]:
        if ((i,j) and (j,i)) not in k:
            k.append((i,j))


df = {'i':[],'j':[]}
for i in range(0,len(k)):
    df['i'].append(k[i][0])
    df['j'].append(k[i][1])
df = pd.DataFrame(df)
df.to_csv('../output/edge-graph.csv')





