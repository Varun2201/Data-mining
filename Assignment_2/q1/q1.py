#!/usr/bin/env python
# coding: utf-8

import pandas as pd

census = pd.read_csv('../data/Census_clean.csv')
language = pd.read_csv('../data/C-18.csv')

state = list(language['State_code'].unique())

output = []
for i in state:
    temp_census = census[(census['State']==i) & (census['TRU']=='Total')] 
    temp_language = language[(language['State_code']==i) & (language['Type']=='Total') & (language['Age_grp']=='Total')] 

    one_language = int(temp_census['TOT_P']) - int(temp_language['Person-second'])
    two_language = int(temp_language['Person-second'] - temp_language['Person-third'])
    three_language = int(temp_language['Person-third'])
    
    one_language = (one_language/int(temp_census['TOT_P']))*100
    two_language = (two_language/int(temp_census['TOT_P']))*100
    three_language = (three_language/int(temp_census['TOT_P']))*100

    output.append([i,one_language,two_language,three_language])


output = pd.DataFrame(output,columns=['state-code','percent-one','percent-two','percent-three'])
output.to_csv('../output/percent-india.csv',index=False)

