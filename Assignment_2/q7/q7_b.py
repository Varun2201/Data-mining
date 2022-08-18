#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


North = (['JAMMU & KASHMIR' , 'HIMACHAL PRADESH','HARYANA' , 'PUNJAB', 'UTTARAKHAND', 'NCT OF DELHI', 'CHANDIGARH'],'North')
West = (['RAJASTHAN','GUJARAT','MAHARASHTRA','GOA','DADRA & NAGAR HAVELI','DAMAN & DIU'],'West')
Central = (['MADHYA PRADESH','UTTAR PRADESH','CHHATTISGARH'],'Central')
East = (['BIHAR','ODISHA','JHARKHAND','WEST BENGAL'],'East')
South = (['KARNATAKA','KERALA','ANDHRA PRADESH','LAKSHADWEEP','PUDUCHERRY','TAMIL NADU'],'South')
North_east = (['ASSAM','SIKKIM','ARUNACHAL PRADESH','MIZORAM','NAGALAND','MANIPUR','TRIPURA','ANDAMAN & NICOBAR ISLANDS','MEGHALAYA'], 'North_east')


# In[8]:


region_list = [North,West,Central,East,South, North_east]


output_b = []

for region in region_list:
    final = []
    for i in region[0]:
        temp = pd.read_csv('../data/c17/'+i+'.csv')
        final.append(temp)

    final = pd.concat(final,ignore_index=True)

    most_language = final['language'].unique()

    total_b = []

    for i in most_language:
        temp = final[final['language']==i]
        count_b = temp['first'].sum()
        total_b.append([count_b,i])


    total_b.sort(reverse=True)
    output_b.append([region[1],total_b[0][1],total_b[1][1],total_b[2][1]])


# In[11]:

output_b.sort()
output_b = pd.DataFrame(output_b,columns=['region','language-1','language-2','language-3'])
output_b.to_csv('../output/region-india-b.csv',index=False)

