import pandas as pd
census = pd.read_csv('../data/Census_clean.csv')
language = pd.read_csv('../data/C-18.csv')

state = list(language['State_code'].unique())

output_2 =[]

for i in state:
    temp_census = census[(census['State']==i) & (census['TRU']=='Total')] 
    temp_language = language[(language['State_code']==i) & (language['Type']=='Total') & (language['Age_grp']=='Total')]

    one_language = int(temp_census['TOT_P']) - int(temp_language['Person-second'])
    two_language = int(temp_language['Person-second'] - temp_language['Person-third'])
    three_language = int(temp_language['Person-third'])

    ratio = two_language/one_language
    output_2.append([i,ratio])

output_2.sort(key=lambda x: x[1],reverse=True)

final =[]
final.extend(output_2[:3])
final.extend([output_2[-1],output_2[-2],output_2[-3]])

final = pd.DataFrame(final,columns=['state-code','2-to-1-ratio'])
final.to_csv('../output/2-to-1-ratio.csv',index=False)
