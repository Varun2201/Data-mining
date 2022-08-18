#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data_ref = pd.read_csv('../data/C-19.csv')
data_total = pd.read_csv('../data/C-08.csv') 


# In[2]:


state = list(data_ref['State_code'].unique())
education_level = list(data_ref['Education_level'].unique())


# In[3]:


output = []
for i in state:
    temp = data_ref[(data_ref['State_code']==i) & (data_ref['Type']=='Total')]
    temp_total = data_total[(data_total['State_Code']==i) &(data_total['Type']=='Total') & (data_total['Age_grp']=='All ages')]
    max_1 = 0
    max_edu_1 = 0
    max_2 = 0
    max_edu_2 = 0
    max_3 = 0
    max_edu_3 = 0

    for j in education_level:
        male = j + '_Male'
        female = j + '_Female'
        m3 = int(temp[temp['Education_level']==j]['Male-third'])
        f3 = int(temp[temp['Education_level']==j]['Female-third'])
        male_t = int(temp_total[male])
        female_t = int(temp_total[female])
        ratio_1 = m3/male_t
        ratio_2 = f3/female_t
        if ratio_1 > max_1:
            max_1 = ratio_1
            max_edu_1 = j
        if ratio_2 > max_2:
            max_2 = ratio_2
            max_edu_2 = j

    output.append([i,max_edu_1,max_1,max_edu_2,max_2])


# In[4]:


output = pd.DataFrame(output,columns=['state/ut','literacy-group-males','ratio-males','literacy-group-females','ratio-females'])
output.to_csv('../output/literacy-gender-a.csv',index=False)


# In[5]:


output = []
for i in state:
    temp = data_ref[(data_ref['State_code']==i) & (data_ref['Type']=='Total')]
    temp_total = data_total[(data_total['State_Code']==i) &(data_total['Type']=='Total') & (data_total['Age_grp']=='All ages')]
    max_1 = 0
    max_edu_1 = 0
    max_2 = 0
    max_edu_2 = 0

    for j in education_level:
        male = j + '_Male'
        female = j + '_Female'
        m3 = int(temp[temp['Education_level']==j]['Male-second']) - int(temp[temp['Education_level']==j]['Male-third'])
        f3 = int(temp[temp['Education_level']==j]['Female-second']) - int(temp[temp['Education_level']==j]['Female-third'])
        male_t = int(temp_total[male])
        female_t = int(temp_total[female])
        ratio_1 = m3/male_t
        ratio_2 = f3/female_t
        if ratio_1 > max_1:
            max_1 = ratio_1
            max_edu_1 = j
        if ratio_2 > max_2:
            max_2 = ratio_2
            max_edu_2 = j

    output.append([i,max_edu_1,max_1,max_edu_2,max_2])


# In[6]:


output = pd.DataFrame(output,columns=['state/ut','literacy-group-males','ratio-males','literacy-group-females','ratio-females'])
output.to_csv('../output/literacy-gender-b.csv',index=False)


# In[7]:


output = []
for i in state:
    temp = data_ref[(data_ref['State_code']==i) & (data_ref['Type']=='Total')]
    temp_total = data_total[(data_total['State_Code']==i) &(data_total['Type']=='Total') & (data_total['Age_grp']=='All ages')]
    max_1 = 0
    max_edu_1 = 0
    max_2 = 0
    max_edu_2 = 0

    for j in education_level:
        male = j + '_Male'
        female = j + '_Female'
        male_t = int(temp_total[male])
        female_t = int(temp_total[female])
        m3 = male_t - int(temp[temp['Education_level']==j]['Male-second'])
        f3 = female_t - int(temp[temp['Education_level']==j]['Female-second'])
        ratio_1 = m3/male_t
        ratio_2 = f3/female_t
        if ratio_1 > max_1:
            max_1 = ratio_1
            max_edu_1 = j
        if ratio_2 > max_2:
            max_2 = ratio_2
            max_edu_2 = j

    output.append([i,max_edu_1,max_1,max_edu_2,max_2])


# In[8]:


output = pd.DataFrame(output,columns=['state/ut','literacy-group-males','ratio-males','literacy-group-females','ratio-females'])
output.to_csv('../output/literacy-gender-c.csv',index=False)


# In[ ]:




