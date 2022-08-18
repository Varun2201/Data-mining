#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd 
from scipy.stats import ttest_1samp

census = pd.read_csv('../data/Census_clean.csv')
language = pd.read_csv('../data/C-18.csv')


# In[11]:


state = language['State_code'].unique()
output_1 = []
output_2 = []
output_3 = []
for i in state:
    temp_census = census[(census['State']==i) & (census['TRU']=='Total')] 
    temp_language = language[(language['State_code']==i) & (language['Type']=='Total') & (language['Age_grp']=='Total')] 

    tot_female_2 = int(temp_language['female-second']) - int(temp_language['female-third'])
    tot_male_2 = int(temp_language['Male-second']) - int(temp_language['Male-third'])

    tot_female_1 = int(temp_census['TOT_F']) - int(temp_language['female-second'])
    tot_male_1 = int(temp_census['TOT_M']) - int(temp_language['Male-second'])

    tot_male_3  = int(temp_language['Male-third'])
    tot_female_3= int(temp_language['female-third'])

    female_prop_3 = int(temp_language['female-third'])/int(temp_census['TOT_F'])
    male_prop_3 = int(temp_language['Male-third'])/int(temp_census['TOT_M'])

    female_prop_2 = tot_female_2/int(temp_census['TOT_F'])
    male_prop_2 = tot_male_2/int(temp_census['TOT_M'])

    female_prop_1 = tot_female_1/int(temp_census['TOT_F'])
    male_prop_1 = tot_male_1/int(temp_census['TOT_M'])

    ratio_1 = tot_male_1/tot_female_1
    ratio_2 = tot_male_2/tot_female_2
    ratio_3 = tot_male_3/tot_female_3

    ratio_final = int(temp_census['TOT_M'])/int(temp_census['TOT_F'])
 
    #chi_sqaure , p_value = chisquare([ratio_1,ratio_2,ratio_3], f_exp=[ratio_final,ratio_final,ratio_final])
    t_value ,p_value = ttest_1samp(a = [ratio_1,ratio_2,ratio_3],popmean=ratio_final)
    #print(p_value)

    output_1.append([i,male_prop_1*100,female_prop_1*100,p_value])
    output_2.append([i,male_prop_2*100,female_prop_2*100,p_value])
    output_3.append([i,male_prop_3*100,female_prop_3*100,p_value])


# In[15]:


output_1 = pd.DataFrame(output_1,columns=['state/ut','male-percentage','female-percentage','p-value'])
output_1.to_csv('../output/gender-india-a.csv')
output_2 = pd.DataFrame(output_2,columns=['state/ut','male-percentage','female-percentage','p-value'])
output_2.to_csv('../output/gender-india-b.csv')
output_3 = pd.DataFrame(output_3,columns=['state/ut','male-percentage','female-percentage','p-value'])
output_3.to_csv('../output/gender-india-c.csv')


# In[ ]:




