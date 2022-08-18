#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 

total_pop = pd.read_csv('../data/C-14.csv')
data_ref = pd.read_csv('../data/C-18.csv')


# In[2]:


state = list(data_ref['State_code'].unique())
age = list(data_ref['Age_grp'].unique())

output = []


# In[3]:


for i in state:
    max = 0
    max_age = 0
    for j in age:
        try:
            temp_data = int(data_ref[(data_ref['State_code']==i) & (data_ref['Age_grp']==j) & (data_ref['Type']=='Total')]['Person-third'])
            total = int(total_pop[(total_pop['State_code']==i) & (total_pop['Age_grp']==j)]['T_P'])

            ratio = temp_data/total
            if ratio > max:
                max = ratio
                max_age = j
        except:
            pass
    output.append([i,max_age,max*100])


# In[4]:


output = pd.DataFrame(output,columns=['state/ut','age-group','perecentage'])
output.to_csv('../output/age-india.csv',index=False)

