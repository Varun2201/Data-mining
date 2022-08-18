import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
data = pd.read_csv('../data/vaccine.csv')
inc = datetime.timedelta(days=1)

temp = data[data['District_Key']=='AP_Anantapur']

stdat = datetime.date(2021,1,16)
tempdat = stdat
enddat = datetime.date(2021,8,14)
currentdat = stdat
ltotald1 = 0
ltotald2 = 0

d_id = list(data['District_Key'])
d_id.sort()
mo = []
for i in d_id:
    temp = data[data['District_Key']==i]
    stdat = datetime.date(2021,1,15)
    tempdat = stdat
    enddat = datetime.date(2021,8,14)
    currentdat = stdat
    ltotald1 = 0
    ltotald2 = 0
    count = 1
    while currentdat < enddat:
        timedata = currentdat + relativedelta(months=1)
        total_dose1 = 0
        total_dose2 = 0
        while currentdat < timedata:
            tempdat = currentdat.strftime('%d/%m/%Y')
            try:
                    x = tempdat+'.3'
                    y = tempdat+'.4'
                    dose1 = int(temp[x]) - ltotald1
                    dose2 = int(temp[y]) - ltotald2
                    ltotald1 = int(temp[x])
                    ltotald2 = int(temp[y])
            except:
                    dose1 = 0
                    dose2 = 0
            currentdat = currentdat +inc
            total_dose1 = dose1 +total_dose1
            total_dose2 = dose2 +total_dose2
        mo.append([i,count,total_dose1,total_dose2])
        count = count + 1
    
mo = pd.DataFrame(mo,columns=['districtid','monthid','dose1','dose2'])
mo.to_csv('../output/district-vaccinated-count-month.csv')

s_id = list(data['State_Code'].unique())
s_id.sort()
mo = []
for i in s_id:
    temp = data[data['State_Code']==i]
    stdat = datetime.date(2021,1,15)
    tempdat = stdat
    enddat = datetime.date(2021,8,14)
    currentdat = stdat
    ltotald1 = 0
    ltotald2 = 0
    count = 1
    while currentdat < enddat:
        timedata = currentdat + relativedelta(months=1)
        total_dose1 = 0
        total_dose2 = 0
        while currentdat < timedata:
            tempdat = currentdat.strftime('%d/%m/%Y')
            try:
                    x = tempdat+'.3'
                    y = tempdat+'.4'
                    dose1 = int(temp[x].sum()) - ltotald1
                    dose2 = int(temp[y].sum()) - ltotald2
                    ltotald1 = int(temp[x].sum())
                    ltotald2 = int(temp[y].sum())
            except:
                    dose1 = 0
                    dose2 = 0
            currentdat = currentdat +inc
            total_dose1 = dose1 +total_dose1
            total_dose2 = dose2 +total_dose2
        mo.append([i,count,total_dose1,total_dose2])
        count = count + 1


mo = pd.DataFrame(mo,columns=['stateid','monthid','dose1','dose2'])
mo.to_csv('../output/state-vaccinated-count-month.csv')




