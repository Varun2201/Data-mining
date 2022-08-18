#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
census = pd.read_csv('../data/Census_clean.csv')
language = pd.read_csv('../data/C-18.csv')


# In[16]:


state = list(language['State_code'].unique())
output_3 =[]

for i in state:
    temp_census = census[(census['State']==i) & (census['TRU']=='Total')] 
    temp_language = language[(language['State_code']==i) & (language['Type']=='Total') & (language['Age_grp']=='Total')]

    two_language = int(temp_language['Person-second'] - temp_language['Person-third'])
    three_language = int(temp_language['Person-third'])

    ratio = three_language/two_language
    output_3.append([i,ratio])


# In[17]:


output_3.sort(key=lambda x: x[1],reverse=True)
final =[]
final.extend(output_3[:3])
final.extend([output_3[-1],output_3[-2],output_3[-3]])

final = pd.DataFrame(final,columns=['state-code','3-to-2-ratio'])
final.to_csv('../output/3-to-2-ratio.csv',index=False)


# In[18]:




