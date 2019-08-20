#2- Entre os 30 congressistas que mais gastaram no país, quantos foram reeleitos?
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

congressPersons = congressPersons.head(30)
# we're checking 2019 to see if these congressmen appear again after the election 
# or, in others words, if they were reelected. 
df2 = df[df.numAno.isin([2019])]

reelected = pd.Series(congressPersons.ideCadastro.isin(df2.ideCadastro).values.astype(bool), 
                      congressPersons.ideCadastro.values).to_frame()
# ideCadastro values were working as index, the following line makes it a column and resets the index
reelected.reset_index(level=0, inplace=True)
# renaming columns so it matches congressPersons' column names
reelected.columns = ['ideCadastro','Reeleito?']
reelected = pd.merge(reelected, congressPersons, on='ideCadastro')

#Making tratment for column names
reelected.rename(columns={'ideCadastro':'ID de Cadastro', 'txNomeParlamentar':'Nome do Parlamentar', 'valor':'Valor Total Gasto'}, 
            inplace=True)
booleanDictionary = {True: 'Sim', False: 'Não'}
reelected = reelected.replace(booleanDictionary)

print (reelected)