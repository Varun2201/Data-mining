import pandas as pd
import datetime
import math 
from dateutil.relativedelta import relativedelta
inc = datetime.timedelta(days=1)

data_ref = pd.read_csv('../data/vaccine.csv')
data_cen = pd.read_csv('../data/census.csv')


stdat = datetime.date(2021,8,8)
enddat = datetime.date(2021,8,14)
edat = enddat.strftime('%d/%m/%Y')
sdat = stdat.strftime('%d/%m/%Y')
d1 = edat + '.3'
d2 = sdat + '.3'

state_ratio = []
state_id = list(data_ref['State_Code'].unique())
state_id.sort()

for i in state_id: 
    temp=data_ref[data_ref['State_Code']==i]
    temp_cen = data_cen[data_cen['Name']==i]
    if not(temp.empty) and not(temp_cen.empty):
        diff = int(temp[d1].sum()) - int(temp[d2].sum())
        total_pop_rem = int(temp_cen['TOT_P']) - int(temp[d1].sum())
        if total_pop_rem > 0 :
            last_date = math.ceil(total_pop_rem/diff)
            timedate = enddat + 7*inc*last_date
        else:
            total_pop_rem = 0
            timedate = enddat
        state_ratio.append([i,total_pop_rem,diff,str(timedate)])


state_ratio = pd.DataFrame(state_ratio,columns=['stateid','populationleft','rateofvaccination','date'])
state_ratio.to_csv('../output/complete-vaccination.csv')
