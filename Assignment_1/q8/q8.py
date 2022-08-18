import pandas as pd 
import datetime

data_ref = pd.read_csv('../data/vaccine.csv')
data_cen = pd.read_csv('../data/census.csv')

dis_ratio = []
d_id = list(data_ref['District_Key'].unique())
d_id.sort()

for i in d_id: 
    temp=data_ref[data_ref['District_Key']==i]
    temp_cen = data_cen[data_cen['Name']==i]
    if not(temp.empty) and not(temp_cen.empty):
        enddat = datetime.date(2021,8,14)
        edat = enddat.strftime('%d/%m/%Y')
        d1 = edat + '.3'
        d2 = edat + '.4'
        dose1_vac = int(temp[d1])
        dose2_vac = int(temp[d2])
        vac_dose1 = float(dose1_vac / temp_cen['TOT_P'])
        vac_dose2 = float(dose2_vac/temp_cen['TOT_P'])
        dis_ratio.append([i,vac_dose1,vac_dose2])

dis_ratio.sort(key=lambda x: x[1])

state_ratio = []
state_id = list(data_ref['State_Code'].unique())
state_id.sort()

for i in state_id: 
    temp=data_ref[data_ref['State_Code']==i]
    temp_cen = data_cen[data_cen['Name']==i]
    if not(temp.empty) and not(temp_cen.empty):
        dose1_vac = int(temp[d1].sum())
        dose2_vac = int(temp[d2].sum())
        vac_dose1 = float(dose1_vac / temp_cen['TOT_P'])
        vac_dose2 = float(dose2_vac/temp_cen['TOT_P'])
        state_ratio.append([i,vac_dose1,vac_dose2])

state_ratio.sort(key=lambda x: x[1])

overall = []
dose1_vac = int(data_ref[d1].sum())
dose2_vac = int(data_ref[d2].sum())
vac_dose1 = float(dose1_vac/ data_cen[data_cen['Name']=='India']['TOT_P'])
vac_dose2 = float(dose2_vac/data_cen[data_cen['Name']=='India']['TOT_P'])
overall.append(['IN',vac_dose1,vac_dose2])



dis_ratio = pd.DataFrame(dis_ratio,columns=['districtid','vaccinationdose1ratio','vaccinationdose2ratio'])
dis_ratio.to_csv('../output/district-vaccianted-dose-ratio.csv')

state_ratio = pd.DataFrame(state_ratio,columns=['stateid','vaccinationdose1ratio','vaccinationdose2ratio'])
state_ratio.to_csv('../output/state-vaccianted-dose-ratio.csv')

overall = pd.DataFrame(overall,columns=['Country','vaccinationdose1ratio','vaccinationdose2ratio'])
overall.to_csv('../output/overall-vaccianted-dose-ratio.csv')



