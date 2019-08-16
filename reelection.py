# -*- coding: utf-8 -*-
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

df = pd.read_csv('2015-2019.csv')
df = df.drop(columns=['nuCarteiraParlamentar', 'codLegislatura', 'txtFornecedor', 
                      'txtCNPJCPF', 'nuCarteiraParlamentar', 'indTipoDocumento', 
                      'vlrDocumento', 'vlrGlosa', 'numParcela', 'txtTrecho', 'numLote'])
#We want to get the top spenders from 2015 to 2018
years = [2015, 2016, 2017, 2018]
#Filtering dataset with years
df1 = df[df.numAno.isin(years)]

congressPersons = df1.groupby(['ideCadastro', 'txNomeParlamentar'])['vlrLiquido'].sum().to_frame(name = 'valor').reset_index()
congressPersons = congressPersons.sort_values(['valor'], ascending=False)
congressPersons = congressPersons.astype({"ideCadastro": int})

print(congressPersons.head(30))

df2 = df[df.numAno.isin([2019])]

# https://stackoverflow.com/questions/50449088/check-if-value-from-one-dataframe-exists-in-another-dataframe
#topValues.ideCadastro.isin(df2.ideCadastro).astype(bool)
#print(pd.Series(topValues.ideCadastro.isin(df2.ideCadastro).values.astype(bool), topValues.ideCadastro.values))
