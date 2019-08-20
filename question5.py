#5- Existe alguma correlação entre gastos e quantidade de propostas?
# -*- coding: utf-8 -*-
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # plot graphs

dfProp = pd.read_csv('propostas2015-2018.csv', low_memory=False, usecols=['idDeputadoAutor', 'tipoAutor'])
dfProp = dfProp[dfProp.tipoAutor.isin(['Deputado'])]

proposalsCount = dfProp.groupby(['idDeputadoAutor']).size().to_frame('quantidadePropostas').reset_index().sort_values(by='quantidadePropostas', ascending=False)

dfSpend = pd.read_csv('2015-2019.csv')
congressPersons = dfSpend.groupby(['ideCadastro', 'txNomeParlamentar'])['vlrLiquido'].sum().to_frame(name = 'valorGasto').reset_index()
congressPersons.rename(columns={'ideCadastro':'idDeputadoAutor'}, inplace=True)

output = pd.merge(proposalsCount, congressPersons, on='idDeputadoAutor')

ax1 = output.plot.scatter(x='valorGasto', y='quantidadePropostas', c='DarkBlue')

print (output['valorGasto'].corr(output['quantidadePropostas']))

plt.show()