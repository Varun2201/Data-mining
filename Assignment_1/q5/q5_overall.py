import pandas as pd
import  datetime
data = pd.read_csv('../data/vaccine.csv')


'''remove = ['kheri', 'konkan division', 'niwari', 'noklak', 'parbhani', 'pattanamtitta','chengalpattu', 'gaurela pendra marwahi', 'nicobars', 'north and middle andaman', 'saraikela-kharsawan',
'south andaman', 'tenkasi', 'tirupathur', 'yanam','mumbai city']

for i in remove:
    try:
       data = data.drop(data[data['District']==i.title()].index)
    except:
        pass
data = data.drop(data[data['District']=='Andaman and Nicobar Islands'].index)'''

data_ref = data
data_ref=data_ref.fillna(0)

'''
stdat = datetime.date(2021,1,15)
enddat = datetime.date(2021,8,14)
tempdat = stdat.strftime('%d/%m/%Y')
currentdat = stdat 
tempdat = currentdat.strftime('%d/%m/%Y')'''

vaccine_od = []
d_id = list(data_ref['District_Key'])
d_id.sort()
ltotald1 = 0
ltotald2 = 0
for i in d_id:
    temp = data_ref[data_ref['District_Key'] == i ]
    stdat = datetime.date(2021,1,16)
    enddat = datetime.date(2021,8,15)
    tempdat = stdat.strftime('%d/%m/%Y')
    edat = enddat.strftime('%d/%m/%Y')
    ltotald1 = 0
    ltotald2 = 0
    x = tempdat+'.3'
    y = tempdat+'.4'
    xe = edat + '.3'
    ye = edat + '.4'
    overall_dose1 = int(temp[xe]) - int(temp[x])
    overall_dose2 = int(temp[ye]) - int(temp[y]) 
    vaccine_od.append([i,overall_dose1,overall_dose2])


s_id = list(data_ref['State_Code'].unique())
s_id.sort()


vaccine_so = []
for i in s_id:
    temp = data_ref[data_ref['State_Code'] == i ]
    overall_dose1 = 0
    overall_dose2 = 0
    stdat = datetime.date(2021,1,16)
    enddat = datetime.date(2021,8,15)
    tempdat = stdat.strftime('%d/%m/%Y')
    edat = enddat.strftime('%d/%m/%Y')
    x = tempdat+'.3'
    y = tempdat+'.4'
    xe = edat + '.3'
    ye = edat + '.4'
    overall_dose1 = int(temp[xe].sum()) - int(temp[x].sum())
    overall_dose2 = int(temp[ye].sum()) - int(temp[y].sum()) 
    vaccine_so.append([i,overall_dose1,overall_dose2])
    vaccine_so.append([i,overall_dose1,overall_dose2])


vaccine_od = pd.DataFrame(vaccine_od,columns=['districtid','dose1','dose2'])
vaccine_so = pd.DataFrame(vaccine_so,columns=['stateid','dose1','dose2'])
vaccine_od.to_csv('../output/district-vaccinated-count-overall.csv')
vaccine_so.to_csv('../output/state-vaccinated-count-overall.csv')

