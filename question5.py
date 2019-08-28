#5- Existe alguma correlação entre gastos e quantidade de propostas?
# -*- coding: utf-8 -*-
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # plot graphs
import seaborn as sns # beautify graphs

dfProp = pd.read_csv('propostas2015-2018.csv', low_memory=False, usecols=['idDeputadoAutor', 'tipoAutor'])
dfProp = dfProp[dfProp.tipoAutor.isin(['Deputado'])]

proposalsCount = dfProp.groupby(['idDeputadoAutor']).size().to_frame('quantidadePropostas').reset_index().sort_values(by='quantidadePropostas', ascending=False)

dfSpend = pd.read_csv('2015-2019.csv')
#We want to get the spends from 2015 to 2018
years = [2015, 2016, 2017, 2018]
#Filtering dataset with years
dfSpend = dfSpend[dfSpend.numAno.isin(years)]
congressPersons = dfSpend.groupby(['ideCadastro', 'txNomeParlamentar'])['vlrLiquido'].sum().to_frame(name = 'valorGasto').reset_index()
congressPersons.rename(columns={'ideCadastro':'idDeputadoAutor'}, inplace=True)

output = pd.merge(proposalsCount, congressPersons, on='idDeputadoAutor')

sns.lmplot('valorGasto', 'quantidadePropostas', data=output, fit_reg=False).set(ylabel='Quantidade de propostas', xlabel='Valor gasto pelo deputado')

print (output['valorGasto'].corr(output['quantidadePropostas']))

plt.show()