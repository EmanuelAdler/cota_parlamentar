import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

df = pd.read_csv('Gastos-Quota-Parlamentar.csv', dtype={'reimbursement_numbers': object})
#Dropping unnecessary columns
df = df.drop(columns=['congressperson_document', 'term_id', 'supplier', 'cnpj_cpf', 'document_number', 'document_type', 'document_value', 'remark_value', 'installment', 'passenger', 'leg_of_the_trip', 'batch_number'])

#Selecting years we will use
years = [2011]
#Filtering dataset with years
df1 = df[df.year.isin(years)]

partySpendings = df1.groupby(['party'])['net_values'].sum()
congressPersonTotal = df1.groupby(['party'])['congressperson_id'].nunique()

df2 = pd.merge(partySpendings, congressPersonTotal, on='party')

#df2['avg'] = df2[['net_values', 'congressperson_id']].mean(axis=1)
df2['avg'] = df2['net_values']/df2['congressperson_id']

df2 = df2.sort_values(['avg'], ascending=False)

print (df2)