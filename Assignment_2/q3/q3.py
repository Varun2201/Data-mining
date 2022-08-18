#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd 
from scipy.stats import ttest_1samp

census = pd.read_csv('../data/Census_clean.csv')
language = pd.read_csv('../data/C-18.csv')


# In[6]:


state = language['State_code'].unique()
output_1 = []
output_2 = []
output_3 = []

for i in state:
    urban_census = census[(census['State']==i) & (census['TRU']=='Urban')]
    rural_census = census[(census['State']==i) & (census['TRU']=='Rural')]

    urban_language = language[(language['State_code']==i) & (language['Type']=='Urban') & (language['Age_grp']=='Total')]
    rural_language = language[(language['State_code']==i) & (language['Type']=='Rural') & (language['Age_grp']=='Total')]


    tot_urban_3 = int(urban_language['Person-third'])
    tot_rural_3 = int(rural_language['Person-third'])

    tot_urban_2 = int(urban_language['Person-second']) - int(urban_language['Person-third'])
    tot_rural_2 = int(rural_language['Person-second']) - int(rural_language['Person-third'])

    tot_urban_1 = int(urban_census['TOT_P']) - int(urban_language['Person-second'])
    tot_rural_1 = int(rural_census['TOT_P']) - int(rural_language['Person-second'])

    ratio_1 = tot_urban_1/tot_rural_1
    ratio_2 = tot_urban_2/tot_rural_2
    ratio_3 = tot_urban_3/tot_rural_3


    ratio_final = int(urban_census['TOT_P'])/int(rural_census['TOT_P'])

    urban_prop_3 = int(urban_language['Person-third'])/int(urban_census['TOT_P'])
    rural_prop_3 = int(rural_language['Person-third'])/int(rural_census['TOT_P'])

    urban_prop_2 = tot_urban_2/int(urban_census['TOT_P'])
    rural_prop_2 = tot_rural_2/int(rural_census['TOT_P'])

    urban_prop_1 = tot_urban_1/int(urban_census['TOT_P'])
    rural_prop_1 = tot_rural_1/int(rural_census['TOT_P'])

    t_value ,p_value = ttest_1samp(a = [ratio_1,ratio_2,ratio_3],popmean=ratio_final)

    output_1.append([i,urban_prop_1*100,rural_prop_1*100,p_value]) 
    output_2.append([i,urban_prop_2*100,rural_prop_2*100,p_value]) 
    output_3.append([i,urban_prop_3*100,rural_prop_3*100,p_value])


# In[7]:


output_1 = pd.DataFrame(output_1,columns=['state/ut','urban-percentage','rural-percentage','p-value'])
output_1.to_csv('../output/geography-india-a.csv')
output_2 = pd.DataFrame(output_2,columns=['state/ut','urban-percentage','rural-percentage','p-value'])
output_2.to_csv('../output/geography-india-b.csv')
output_3 = pd.DataFrame(output_3,columns=['state/ut','urban-percentage','rural-percentage','p-value'])
output_3.to_csv('../output/geography-india-c.csv')


# In[ ]:




