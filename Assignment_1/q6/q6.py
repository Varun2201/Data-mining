import pandas as pd
import datetime


data_ref = pd.read_csv('../data/vaccine.csv')
data_cen = pd.read_csv('../data/census.csv')
data_ref = data_ref.fillna(0)

d_id = list(data_ref['District_Key'].unique())

dis_ratio = []
d_id = list(data_ref['District_Key'].unique())
d_id.sort()

for i in d_id: 
    temp=data_ref[data_ref['District_Key']==i]
    temp_cen = data_cen[data_cen['Name']==i]
    if not(temp.empty) and not(temp_cen.empty):
        enddat = datetime.date(2021,8,14)
        edat = enddat.strftime('%d/%m/%Y')
        me = edat + '.5'
        fe = edat + '.6'
        female_vac = int(temp[fe])
        male_vac = int(temp[me])
        vac_ratio = female_vac/male_vac
        pop_ratio = float(temp_cen['TOT_F']/temp_cen['TOT_M'])
        ratio_ratio = float(vac_ratio/pop_ratio)
        dis_ratio.append([i,vac_ratio,pop_ratio,ratio_ratio])

dis_ratio.sort(key=lambda x: x[3])



state_ratio = []
s_id = list(data_ref['State_Code'].unique())
s_id.sort()
for i in s_id: 
    temp=data_ref[data_ref['State_Code']==i]
    temp_cen = data_cen[data_cen['Name']==i]
    if not(temp.empty) and not(temp_cen.empty):
        #enddat = datetime.date(2021,8,14)
        #edat = enddat.strftime('%d/%m/%Y')
        #me = edat + '.5'
        #fe = edat + '.6'
        female_vac = int(temp[fe].sum())
        male_vac = int(temp[me].sum())
        vac_ratio = female_vac/male_vac
        pop_ratio = float(temp_cen['TOT_F']/temp_cen['TOT_M'])
        ratio_ratio = float(vac_ratio/pop_ratio)
        state_ratio.append([i,vac_ratio,pop_ratio,ratio_ratio])
state_ratio.sort(key=lambda x: x[3])


female_vac = data_ref[fe].sum()
male_vac = data_ref[me].sum()
vac_ratio = female_vac/male_vac
pop_ratio = data_cen.iloc[0]['TOT_F']/data_cen.iloc[0]['TOT_M']
ratio_ratio = vac_ratio/pop_ratio



state_ratio = pd.DataFrame(state_ratio,columns=['stateid','vacciantionratio','populationratio','ratioofratios'])
dis_ratio = pd.DataFrame(dis_ratio,columns=['districtid','vacciantionratio','populationratio','ratioofratios'])
state_ratio.to_csv('../output/state-vaccination-population-ratio.csv')
dis_ratio.to_csv('../output/district-vaccination-population-ratio.csv')

x = ['IN',vac_ratio,pop_ratio,ratio_ratio]

x = pd.DataFrame([x],columns=['country','vacciantionratio','populationratio','ratioofratios'])
x.to_csv('../output/overall-vaccination-population-ratio.csv')



