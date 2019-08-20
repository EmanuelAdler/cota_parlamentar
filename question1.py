# -*- coding: utf-8 -*-
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # plot graphs

dfEven = pd.read_csv('eventos2015-2018.csv', low_memory=False, usecols=['idDeputado'])

eventsCount = dfEven.groupby(['idDeputado']).size().to_frame('quantidadeEventos').reset_index().sort_values(by='quantidadeEventos', ascending=False)

dfSpend = pd.read_csv('2015-2019.csv')
congressPersons = dfSpend.groupby(['ideCadastro', 'txNomeParlamentar'])['vlrLiquido'].sum().to_frame(name = 'valorGasto').reset_index()
congressPersons.rename(columns={'ideCadastro':'idDeputado'}, inplace=True)

output = pd.merge(eventsCount, congressPersons, on='idDeputado')

ax1 = output.plot.scatter(x='valorGasto', y='quantidadeEventos', c='DarkBlue')

plt.show()

print (output['valorGasto'].corr(output['quantidadeEventos']))