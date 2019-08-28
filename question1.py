#1- Existe alguma correlação entre gastos e assiduidade em eventos da casa?
# -*- coding: utf-8 -*-
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # plot graphs
import seaborn as sns # beautify graphs

dfEven = pd.read_csv('eventos2015-2018.csv', low_memory=False, usecols=['idDeputado'])

eventsCount = dfEven.groupby(['idDeputado']).size().to_frame('quantidadeEventos').reset_index().sort_values(by='quantidadeEventos', ascending=False)

dfSpend = pd.read_csv('2015-2019.csv')
dfSpend = pd.read_csv('2015-2019.csv')
#We want to get the spends from 2015 to 2018
years = [2015, 2016, 2017, 2018]
#Filtering dataset with years
dfSpend = dfSpend[dfSpend.numAno.isin(years)]
congressPersons = dfSpend.groupby(['ideCadastro', 'txNomeParlamentar'])['vlrLiquido'].sum().to_frame(name = 'valorGasto').reset_index()
congressPersons.rename(columns={'ideCadastro':'idDeputado'}, inplace=True)

output = pd.merge(eventsCount, congressPersons, on='idDeputado')
sns.lmplot('valorGasto', 'quantidadeEventos', data=output, fit_reg=False).set(ylabel='Quantidade de eventos', xlabel='Valor gasto pelo deputado')

print (output['valorGasto'].corr(output['quantidadeEventos']))

plt.show()