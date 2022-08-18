import pandas as pd 
from dateutil.relativedelta import relativedelta
import  datetime
inc = datetime.timedelta(days=1)
data = pd.read_csv('../data/vaccine.csv')
#data = data.drop(0)
data_ref = pd.read_csv('../data/districts.csv')

z= []
for i in range(0,len(data)):
    state = data.iloc[i]['State']
    district = data.iloc[i]['District']
    district_key = data.iloc[i]['District_Key']
    temp = data_ref[(data_ref['State']==state) & (data_ref['District']==district)]
    if not(temp.empty):
        stdat = datetime.date(2020,3,15)
        tempdat = stdat
        enddat = datetime.date(2021,8,14) 
        cases = 0
        ltotal = 0
        count = 1
        while tempdat < enddat:
            tempdat = tempdat + 7*inc
            cases = 0     
            try:
                c = int(temp[temp['Date']==str(tempdat)]['Confirmed']) - ltotal
                ltotal = int(temp[temp['Date']==str(tempdat)]['Confirmed'])
            except:
                c = 0
            cases = cases + c
            z.append((district_key,count,cases))
            count = count + 1


m = []
for i in range(0,len(data)):
    state = data.iloc[i]['State']
    district = data.iloc[i]['District']
    district_key = data.iloc[i]['District_Key']
    temp = data_ref[(data_ref['State']==state) & (data_ref['District']==district)]
    if not(temp.empty):
        stdat = datetime.date(2020,3,15)
        tempdat = stdat
        enddat = datetime.date(2021,8,14) 
        cases = 0
        ltotal = 0
        count = 1
        while tempdat < enddat:
            tempdat = tempdat + relativedelta(months=1)
            cases = 0
            #while tempdat < timedata:
            try:
                c = int(temp[temp['Date']==str(tempdat)]['Confirmed']) - ltotal
                ltotal = int(temp[temp['Date']==str(tempdat)]['Confirmed'])
            except:
                c = 0
            if c < 0:
                c = 0
            tempdat = tempdat + inc
            cases = cases + c
            m.append((district_key,count,cases))
            count = count + 1


o = []
for i in range(0,len(data)):
    state = data.iloc[i]['State']
    district = data.iloc[i]['District']
    district_key = data.iloc[i]['District_Key']
    temp = data_ref[(data_ref['State']==state) & (data_ref['District']==district)]
    if not(temp.empty):
        stdat = datetime.date(2020,3,15)
        tempdat = stdat
        enddat = datetime.date(2021,8,14) 
        cases = 0
        ltotal = 0
        count = 1
        #while tempdat < enddat:
        try:
            c = int(temp[temp['Date']==str(enddat)]['Confirmed']) - ltotal
            ltotal = int(temp[temp['Date']==str(enddat)]['Confirmed'])
        except:
            c = 0
        if c < 0:
            c = 0
        tempdat = tempdat + inc
        cases = cases + c
        o.append((district_key,cases))


df = {'districtid' : [],'weekid' :[],'cases': []}
z.sort()
for i in z:
    df['districtid'].append(i[0])
    df['weekid'].append(i[1])
    df['cases'].append(i[2])


df = pd.DataFrame(df)
df.to_csv('../output/cases-week.csv')


df = {'districtid' : [],'monthid' :[],'cases': []}
m.sort()
for i in m:
    df['districtid'].append(i[0])
    df['monthid'].append(i[1])
    df['cases'].append(i[2])
df = pd.DataFrame(df)
df.to_csv('../output/cases-month.csv')


df = {'districtid':[], 'cases' :[] }
o.sort()
for i in o:
    df['districtid'].append(i[0])
    df['cases'].append(i[1])
df = pd.DataFrame(df)
df.to_csv('../output/cases-overall.csv')






