import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
inc = datetime.timedelta(days=1)

data = pd.read_csv('../data/vaccine.csv')
data_ref = pd.read_csv('../data/districts.csv')

state = {}
data1 = data[['State','State_Code']].drop_duplicates()
for i in range(0,len(data1)):
    state[data1.iloc[i]['State']] = data1.iloc[i]['State_Code']
peak={}
for i in state:
    state_id = state[i]
    temp = data_ref[data_ref['State']==i]
    if not(temp.empty):
        stdat = datetime.date(2020,3,15)
        tempdat = stdat
        enddat = datetime.date(2021,8,14)
        wdat = datetime.date(2020,3,19)
        z= []
        cases = 0
        ltotal = 0
        ltotal1=0
        count = 1
        while tempdat <= enddat and wdat <= enddat :
            cases = 0     
            tempdat = tempdat + 7*inc
            #for i in range(7):
            try:
                c = int(temp[temp['Date']==str(tempdat)]['Confirmed'].sum()) - ltotal 
                ltotal = int(temp[temp['Date']==str(tempdat)]['Confirmed'].sum())
            except:
                c = 0
            if c < 0:
                c = 0
            cases = cases + c
            z.append((count,cases))
            count = count + 1
            wdat = wdat + 7*inc
            cases = 0
            #for i in range(7):
            try:
                c = int(temp[temp['Date']==str(wdat)]['Confirmed'].sum()) - ltotal1
                ltotal1 = int(temp[temp['Date']==str(wdat)]['Confirmed'].sum())
            except:
                c = 0
            if c < 0:
                c = 0
            cases = cases + c
           
            z.append((count,cases))
            count = count + 1
        count = 0
        max1 = 0
        week = 0
        flag = 0
        x = [] 
        for i in z: 
            if i[1] > max1:
                if flag ==1:
                    max1 = i[1]
                    week = i[0]
                else :
                    count = count +1
            if i[1] < max1 and flag==1:
                count=count-1 
            if i[1] < max1 and flag==0:
                count = 0
            if count > 7 and flag ==0:
                flag = 1
            if count < -15 and flag==1:
                x.append([max1,week])
                max1 = 0
                flag = 0
    x.sort()
    peak[state_id] = x

peak_month = {}
for i in state:
    state_id = state[i]
    temp = data_ref[data_ref['State']==i]
    if not(temp.empty):
        m = []  
        stdat = datetime.date(2020,3,15)
        tempdat = stdat
        enddat = datetime.date(2021,8,14) 
        cases = 0
        #timedata = stdat + relativedelta(months=1)
        ltotal = 0
        rtotal = 0
        count = 1
        while tempdat <= enddat:
            cases = 0
            tempdat = tempdat + relativedelta(months=1)
            #while tempdat < timedata:
            try:
                c = int(temp[temp['Date']==str(tempdat)]['Confirmed'].sum()) - ltotal
                ltotal = int(temp[temp['Date']==str(tempdat)]['Confirmed'].sum())
            except:
                c = 0
            if c < 0:
                c = 0
            cases = cases + c
            m.append((count,cases))
            count = count + 1
        count = 0
        max1 = 0
        flag = 0 
        x=[]
        prev = 0
        for i in range(0,len(m)): 
            try:
                if m[i-1][1] < m[i][1] > m[i+1][1]:
                    x.append([m[i][1],m[i][0]])
            except:
                pass
        x.sort(reverse=True)
        peak_month[state_id] = x

out = []
for i in peak:
    x = []
    try:
        c = max(peak[i][0][1],peak[i][1][1])
        if c in peak[i][0]:
            x.extend([i,peak[i][1][1],peak[i][0][1]])
        else:
            x.extend([i,peak[i][0][1],peak[i][1][1]])
    except:
        x.extend([i,peak[i][0][1],peak[i][0][1]])
    try:
        c = max(peak_month[i][0][1],peak_month[i][1][1])
        if c in peak_month[i][0]:
            x.extend([peak_month[i][1][1],peak_month[i][0][1]])
        else:
            x.extend([peak_month[i][0][1],peak_month[i][1][1]])
    except:
        x.extend([peak_month[i][0][1],peak_month[i][0][1]])
    out.append(x)

out = pd.DataFrame(out,columns=['stateid','wave1-weekid','wave2-weekid','wave1-monthid','wave2-monthid'])
out.to_csv('../output/state-peaks.csv')

y = []
temp = data_ref
stdat = datetime.date(2020,3,15)
tempdat = stdat
enddat = datetime.date(2021,8,14)
wdat = datetime.date(2020,3,19)
z= []
cases = 0
ltotal = 0
count = 1
while tempdat <= enddat and wdat <= enddat :
    cases = 0     
    for i in range(7):
        try:
            c = int(temp[temp['Date']==str(tempdat)]['Confirmed'].sum()) - ltotal
            ltotal = int(temp[temp['Date']==str(tempdat)]['Confirmed'].sum())
        except:
            c = 0
        if c < 0:
            c = 0
        cases = cases + c
        tempdat = tempdat + inc
    z.append((count,cases))
    count = count + 1
    cases = 0
    for i in range(7):
        try:
            c = int(temp[temp['Date']==str(wdat)]['Confirmed'].sum()) - ltotal
            ltotal = int(temp[temp['Date']==str(wdat)]['Confirmed'].sum())
        except:
            c = 0
        if c < 0:
            c = 0
        cases = cases + c
        wdat = wdat + inc
    z.append((count,cases))
    count = count + 1
count = 0
max1 = 0
week = 0
flag = 0
x = [] 
for i in z: 
    if i[1] > max1:
        if flag ==1:
            max1 = i[1]
            week = i[0]
        else :
            count = count +1
    if i[1] < max1 and flag==1:
        count=count-1 
    if i[1] < max1 and flag==0:
        count = 0
    if count > 15 and flag ==0:
        flag = 1
    if count < 0 and flag==1:
        x.append((max1,week))
        max1 = 0
        flag = 0
y.append(x[0][1])
y.append(x[1][1])

m = []  
stdat = datetime.date(2020,3,15)
tempdat = stdat
enddat = datetime.date(2021,8,14) 
cases = 0
#timedata = stdat + relativedelta(months=1)
ltotal = 0
count = 1
while tempdat <= enddat:
    timedata = tempdat + relativedelta(months=1)
    cases = 0
    while tempdat < timedata:
        try:
            c = int(temp[temp['Date']==str(tempdat)]['Confirmed'].sum()) - ltotal
            ltotal = int(temp[temp['Date']==str(tempdat)]['Confirmed'].sum())
        except:
            c = 0
        if c < 0:
            c = 0
        tempdat = tempdat + inc
        cases = cases + c
    m.append((count,cases))
    count = count + 1
count = 0
max1 = 0
flag = 0 
x=[]
prev = 0
for i in range(0,len(m)): 
    try:
        if m[i-1][1] < m[i][1] > m[i+1][1]:
            x.append([m[i][1],m[i][0]])
    except:
        pass
y.append(x[0][1])
y.append(x[1][1])

final = ['IN']
final.extend(y)

final = pd.DataFrame([final],columns=['Country','wave1-weekid','wave2-weekid','wave1-monthid','wave2-monthid'])
final.to_csv('../output/overall-peaks.csv')

