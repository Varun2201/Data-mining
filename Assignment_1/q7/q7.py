#!/usr/bin/python
import pandas as pd
import datetime 

data = pd.read_csv('../data/vaccine.csv')

data_ref = data

d_id = list(data_ref['District_Key'].unique())
d_id.sort()
vaccine_od = []
for i in d_id:
    temp = data_ref[data_ref['District_Key'] == i ]
    stdat = datetime.date(2021,1,16)
    enddat = datetime.date(2021,8,15)
    tempdat = stdat.strftime('%d/%m/%Y')
    edat = enddat.strftime('%d/%m/%Y')
    x = tempdat+'.8'
    y = tempdat+'.9'
    xe = edat + '.8'
    ye = edat + '.9'
    ratio = 0
    try:
        covaxin = int(temp[xe])          
        covishield = int(temp[ye])       
        ratio = covishield/covaxin
    except:
        ratio = 0
    vaccine_od.append([i,ratio])

vaccine_od.sort(key=lambda x: x[1])

s_id = list(data_ref['State_Code'].unique())
s_id.sort()
vaccine_state = []
for i in s_id:
    temp = data_ref[data_ref['State_Code'] == i ]
    stdat = datetime.date(2021,1,16)
    enddat = datetime.date(2021,8,15)
    tempdat = stdat.strftime('%d/%m/%Y')
    edat = enddat.strftime('%d/%m/%Y')
    x = tempdat+'.8'
    y = tempdat+'.9'
    xe = edat + '.8'
    ye = edat + '.9'
    try:
        covaxin = int(temp[xe].sum()) 
        covishield = int(temp[ye].sum())
        ratio = covishield/covaxin
    except:
        ratio = 0
    vaccine_state.append([i,ratio])

vaccine_state.sort(key=lambda x: x[1])


vaccine_od = pd.DataFrame(vaccine_od,columns=['districtid','vaccineratio'])
vaccine_state = pd.DataFrame(vaccine_state,columns=['stateid','vaccineratio'])

vaccine_od = vaccine_od.replace(to_replace=0, value='NA')
vaccine_state = vaccine_state.replace(to_replace=0, value='NA')

vaccine_state.to_csv('../output/state-vaccine-type-ratio.csv')
vaccine_od.to_csv('../output/district-vaccine-type-ratio.csv')


temp = data_ref
#stdat = datetime.date(2021,1,16)
enddat = datetime.date(2021,8,14)
tempdat = stdat.strftime('%d/%m/%Y')
edat = enddat.strftime('%d/%m/%Y')
x = tempdat+'.8'
y = tempdat+'.9'
xe = edat + '.8'
ye = edat + '.9'
try:
    covaxin = int(temp[xe].sum())
    covishield = int(temp[ye].sum()) 
    ratio = covishield/covaxin
except:
    ratio = 'NA'

x = ['IN']
x.append(ratio)
x = pd.DataFrame([x],columns=['Country','Ratio'])
x.to_csv('../output/overall-vaccine-type-ratio.csv')



