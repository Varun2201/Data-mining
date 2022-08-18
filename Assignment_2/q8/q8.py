#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd 

total_pop = pd.read_csv('../data/C-14.csv')
data_ref = pd.read_csv('../data/C-18.csv')


# In[13]:


state = list(data_ref['State_code'].unique())
age = list(data_ref['Age_grp'].unique())


# In[14]:


output = []
for i in state:
    max_female = 0
    max_female_age = 0
    max_male = 0
    max_male_age = 0
    for j in age:
        try:
            temp_data_male = int(data_ref[(data_ref['State_code']==i) & (data_ref['Age_grp']==j) & (data_ref['Type']=='Total')]['Male-third'])
            total_male = int(total_pop[(total_pop['State_code']==i) & (total_pop['Age_grp']==j)]['T_M'])
            
            temp_data_female = int(data_ref[(data_ref['State_code']==i) & (data_ref['Age_grp']==j) & (data_ref['Type']=='Total')]['female-third'])
            total_female = int(total_pop[(total_pop['State_code']==i) & (total_pop['Age_grp']==j)]['T_F'])
            
            ratio_male = temp_data_male/total_male
            ratio_female = temp_data_female/total_female


            if ratio_male > max_male:
                max_male = ratio_male
                max_male_age = j

            if ratio_female > max_female:
                max_female = ratio_female
                max_female_age = j
        except:
            pass
    output.append([i,max_male_age,max_male,max_female_age,max_female])


# In[15]:


output = pd.DataFrame(output,columns=['state/ut','age-group-males','ratio-males','age-group-females','ratio-females'])
output.to_csv('../output/age-gender-a.csv',index=False)


# In[16]:


output = []
for i in state:
    max_female = 0
    max_female_age = 0
    max_male = 0
    max_male_age = 0
    for j in age:
        try:
            temp_data_male = int(data_ref[(data_ref['State_code']==i) & (data_ref['Age_grp']==j) & (data_ref['Type']=='Total')]['Male-third'])
            temp_data_male = int(data_ref[(data_ref['State_code']==i) & (data_ref['Age_grp']==j) & (data_ref['Type']=='Total')]['Male-second']) - temp_data_male
            total_male = int(total_pop[(total_pop['State_code']==i) & (total_pop['Age_grp']==j)]['T_M'])
            
            temp_data_female = int(data_ref[(data_ref['State_code']==i) & (data_ref['Age_grp']==j) & (data_ref['Type']=='Total')]['female-third'])
            temp_data_female = int(data_ref[(data_ref['State_code']==i) & (data_ref['Age_grp']==j) & (data_ref['Type']=='Total')]['female-second']) - temp_data_female
            total_female = int(total_pop[(total_pop['State_code']==i) & (total_pop['Age_grp']==j)]['T_F'])
            
            ratio_male = temp_data_male/total_male
            ratio_female = temp_data_female/total_female


            if ratio_male > max_male:
                max_male = ratio_male
                max_male_age = j

            if ratio_female > max_female:
                max_female = ratio_female
                max_female_age = j
        except:
            pass
    output.append([i,max_male_age,max_male,max_female_age,max_female])


# In[17]:


output = pd.DataFrame(output,columns=['state/ut','age-group-males','ratio-males','age-group-females','ratio-females'])
output.to_csv('../output/age-gender-b.csv',index=False)


# In[18]:


output = []
for i in state:
    max_female = 0
    max_female_age = 0
    max_male = 0
    max_male_age = 0
    for j in age:
        try:
            temp_data_male = int(data_ref[(data_ref['State_code']==i) & (data_ref['Age_grp']==j) & (data_ref['Type']=='Total')]['Male-second']) 
            total_male = int(total_pop[(total_pop['State_code']==i) & (total_pop['Age_grp']==j)]['T_M'])

            temp_data_male = total_male - temp_data_male
            
            temp_data_female = int(data_ref[(data_ref['State_code']==i) & (data_ref['Age_grp']==j) & (data_ref['Type']=='Total')]['female-second'])
            total_female = int(total_pop[(total_pop['State_code']==i) & (total_pop['Age_grp']==j)]['T_F'])

            temp_data_female = total_female - temp_data_female
            
            ratio_male = temp_data_male/total_male
            ratio_female = temp_data_female/total_female


            if ratio_male > max_male:
                max_male = ratio_male
                max_male_age = j

            if ratio_female > max_female:
                max_female = ratio_female
                max_female_age = j
        except:
            pass
    output.append([i,max_male_age,max_male,max_female_age,max_female])


# In[19]:


output = pd.DataFrame(output,columns=['state/ut','age-group-males','ratio-males','age-group-females','ratio-females'])
output.to_csv('../output/age-gender-c.csv',index=False)


# In[ ]:




