import pandas as pd


North = (['JAMMU & KASHMIR' , 'HIMACHAL PRADESH','HARYANA' , 'PUNJAB', 'UTTARAKHAND', 'NCT OF DELHI', 'CHANDIGARH'],'North')
West = (['RAJASTHAN','GUJARAT','MAHARASHTRA','GOA','DADRA & NAGAR HAVELI','DAMAN & DIU'],'West')
Central = (['MADHYA PRADESH','UTTAR PRADESH','CHHATTISGARH'],'Central')
East = (['BIHAR','ODISHA','JHARKHAND','WEST BENGAL'],'East')
South = (['KARNATAKA','KERALA','ANDHRA PRADESH','LAKSHADWEEP','PUDUCHERRY','TAMIL NADU'],'South')
North_east = (['ASSAM','SIKKIM','ARUNACHAL PRADESH','MIZORAM','NAGALAND','MANIPUR','TRIPURA','ANDAMAN & NICOBAR ISLANDS','MEGHALAYA'], 'North_east')

region_list = [North,West,Central,East,South, North_east]

output_a = []

for region in region_list:
    final = []
    for i in region[0]:
        temp = pd.read_csv('../data/c17/'+i+'.csv')
        final.append(temp)

    final = pd.concat(final,ignore_index=True)

    most_language = final['language'].unique()

    total_a = []

    for i in most_language:
        temp = final[final['language']==i]
        count = temp['first'].sum() + temp['second'].sum() + temp['third'].sum()
        total_a.append([count,i])


    total_a.sort(reverse=True)
    output_a.append([region[1],total_a[0][1],total_a[1][1],total_a[2][1]])

output_a.sort()
output_a = pd.DataFrame(output_a,columns=['region','language-1','language-2','language-3'])
output_a.to_csv('../output/region-india-a.csv',index=False)
