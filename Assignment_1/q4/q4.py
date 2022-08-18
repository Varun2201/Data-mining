import pandas as pd 
from dateutil.relativedelta import relativedelta
import  datetime
inc = datetime.timedelta(days=1)

data = pd.read_csv('../data/vaccine.csv')
data = data.drop(0)
data_ref = pd.read_csv('../data/districts.csv')

peak = {}
for i in range(0,len(data)):
    state = data.iloc[i]['State']
    district = data.iloc[i]['District']
    district_key = data.iloc[i]['District_Key']
    temp = data_ref[(data_ref['State']==state) & (data_ref['District']==district)]
    if not(temp.empty):
        stdat = datetime.date(2020,3,15)
        tempdat = stdat
        enddat = datetime.date(2021,8,14)
        wdat = datetime.date(2020,3,19)
        z= []
        cases = 0
        ltotal = 0
        ltotal1 = 0
        count = 1
        while tempdat < enddat and wdat < enddat :
            cases = 0    
            tempdat = tempdat + 7*inc 
            #for i in range(7):
            try:
                c = int(temp[temp['Date']==str(tempdat)]['Confirmed']) - ltotal 
                ltotal = int(temp[temp['Date']==str(tempdat)]['Confirmed'])
            except:
                c = 0
                r = 0
            if c < 0:
                c = 0
                c = c - r 
            cases = cases + c
            z.append((count,cases))
            count = count + 1
            cases = 0
            wdat = wdat + 7*inc
            #for i in range(7):
            try:
                c = int(temp[temp['Date']==str(wdat)]['Confirmed']) - ltotal1
                ltotal1 = int(temp[temp['Date']==str(wdat)]['Confirmed'])
            except:
                c = 0
            if c < 0:
                c = 0
            cases = cases + c 
            z.append((count,cases))
            count = count + 1
        
        x = [] 
        count = 0
        max1 = 0
        week = 0
        flag = 0
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
            if count > 10 and flag ==0:
                flag = 1
            if count < 0 and flag==1:
                x.append([max1,week])
                max1 = 0
                flag = 0
        x.sort(reverse=True)
        peak[district_key] = x


peak_month = {}
for i in range(0,len(data)):
    state = data.iloc[i]['State']
    district = data.iloc[i]['District']
    district_key = data.iloc[i]['District_Key']
    temp = data_ref[(data_ref['State']==state) & (data_ref['District']==district)]
    if not(temp.empty):
        m = []  
        stdat = datetime.date(2020,3,15)
        tempdat = stdat
        enddat = datetime.date(2021,8,14) 
        cases = 0
        ltotal = 0
        count = 1
        while tempdat <= enddat:
            tempdat = tempdat + relativedelta(months=1)
            cases = 0
            try:
                c = int(temp[temp['Date']==str(tempdat)]['Confirmed']) - ltotal 
                ltotal = int(temp[temp['Date']==str(tempdat)]['Confirmed'])
            except:
                c = 0
            if c < 0:
                c = 0
            #tempdat = tempdat + inc
            cases = cases + c - r 
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
        peak_month[district_key] = x


peak_sort = {}
peak_month_sort={}
sort = []
for i in peak:
    sort.append(i)
sort.sort()
for i in sort:
    peak_sort[i] = peak[i]
for i in sort:
    peak_month_sort[i] = peak_month[i]
peak = peak_sort
peak_month = peak_month_sort


out = []
for i in peak:
    x = []
    try:
        if len(peak[i])==0:
            continue
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


out = pd.DataFrame(out,columns=['districtid','wave1-weekid','wave2-weekid','wave1-monthid','wave2-monthid'])
out.to_csv('../output/district-peaks.csv')



