#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

data_ref = pd.read_csv('../data/C-19.csv')
data_total = pd.read_csv('../data/C-08.csv') 


# In[ ]:


state = list(data_ref['State_code'].unique())


# In[ ]:


education_level = list(data_ref['Education_level'].unique())


# In[ ]:


output = []
for i in state:
    temp = data_ref[(data_ref['State_code']==i) & (data_ref['Type']=='Total')]
    temp_total = data_total[(data_total['State_Code']==i) &(data_total['Type']=='Total') & (data_total['Age_grp']=='All ages')]
    max = 0
    max_edu = 0
    for j in education_level:
        st = j + '_Person'
        x = int(temp[temp['Education_level']==j]['Person-third'])
        y = int(temp_total[st])
        ratio = x/y
        if ratio > max:
            max = ratio
            max_edu = j
    output.append([i,max_edu,max*100])
        
        


# In[ ]:


output = pd.DataFrame(output,columns=['state/ut','litreacy-group','percentage'])
output.to_csv('../output/literacy-india.csv',index=False)

