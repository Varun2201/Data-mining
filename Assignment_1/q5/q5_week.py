
import pandas as pd
import  datetime
data = pd.read_csv('../data/vaccine.csv')

inc = datetime.timedelta(days=1)

data_ref = data

d_id = list(data_ref['District_Key'].unique())
d_id.sort()

#temp = data[data['District_Key']=='AP_Anantapur']
w = []
for i in d_id:
    temp = data[data['District_Key']==i]
    stdat = datetime.date(2021,1,10)
    tempdat = stdat
    enddat = datetime.date(2021,8,14)
    currentdat = stdat
    ltotald1 = 0
    ltotald2 = 0
    count = 1
    while currentdat < enddat:
        total_dose1 = 0
        total_dose2 = 0
        for j in range(7):
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
        w.append([i,count,total_dose1,total_dose2])
        count = count + 1

w  =pd.DataFrame(w,columns=['districtid','weekid','dose1','dose2'])
w.to_csv('../output/distrcit-vaccinated-count-week.csv')

s_w = []
s_id = list(data_ref['State_Code'].unique())
s_id.sort()
for i in s_id:
    temp = data[data['State_Code']==i]
    stdat = datetime.date(2021,1,10)
    tempdat = stdat
    enddat = datetime.date(2021,8,14)
    currentdat = stdat
    ltotald1 = 0
    ltotald2 = 0
    count = 1
    while currentdat < enddat:
        total_dose1 = 0
        total_dose2 = 0
        for j in range(7):
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
        s_w.append([i,count,total_dose1,total_dose2])
        count = count + 1


s_w =pd.DataFrame(s_w,columns=['stateid','weekid','dose1','dose2'])
s_w.to_csv('../output/state-vaccinated-count-week.csv')
