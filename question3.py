#3- Dentre os estados da federação, os quatro congressistas que mais gastaram foram reeleitos?
# -*- coding: utf-8 -*-
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import locale
locale.setlocale(locale.LC_ALL, 'pt_br.utf-8')

df = pd.read_csv('2015-2019.csv')
df = df.drop(columns=['nuCarteiraParlamentar', 'codLegislatura', 'txtFornecedor', 
                      'txtCNPJCPF', 'nuCarteiraParlamentar', 'indTipoDocumento', 
                      'vlrDocumento', 'vlrGlosa', 'numParcela', 'txtTrecho', 'numLote'])
#We want to get the top spenders from 2015 to 2018
years = [2015, 2016, 2017, 2018]
#Filtering dataset with years
df1 = df[df.numAno.isin(years)]

congressPersons = df1.groupby(['ideCadastro', 'txNomeParlamentar', 'sgUF'])['vlrLiquido'].sum().to_frame(name = 'valor').reset_index()
congressPersons = congressPersons.sort_values(['valor'], ascending=False)
congressPersons = congressPersons.astype({"ideCadastro": int})

#Defining state names
states = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

#Get top spenders from each state
for i in range(len(states)):
    dfAux = congressPersons[congressPersons.sgUF.isin([states[i]])]
    dfAux = dfAux.head(4)
    if i == 0:
        output = dfAux
    else:
        output = output.append(dfAux)

#print (output)


# we're checking 2019 to see if these congressmen appear again after the election 
# or, in others words, if they were reelected. 
df2 = df[df.numAno.isin([2019])]

reelected = pd.Series(output.ideCadastro.isin(df2.ideCadastro).values.astype(bool), 
                      output.ideCadastro.values).to_frame()
# ideCadastro values were working as index, the following line makes it a column and resets the index
reelected.reset_index(level=0, inplace=True)
# renaming columns so it matches congressPersons' column names
reelected.columns = ['ideCadastro','Reeleito?']
reelected = pd.merge(reelected, output, on='ideCadastro')

#Making tratment for column names
reelected.rename(columns={'ideCadastro':'ID de Cadastro', 'txNomeParlamentar':'Nome do Parlamentar', 'sgUF': 'Estado', 'valor':'Valor Total Gasto'}, 
            inplace=True)
booleanDictionary = {True: 'Sim', False: 'Não'}
reelected = reelected.replace(booleanDictionary)
reelected = reelected[['Nome do Parlamentar', 'Estado', 'Valor Total Gasto', 'Reeleito?']]
reelected['Valor Total Gasto'] = reelected['Valor Total Gasto'].map(locale.currency)


#print (reelected)
#tfile = open('stateReelection.txt', 'w+')
#tfile.write(reelected.to_string())
#tfile.close()
reelected.to_csv(r'stateReelection.csv', index = None, header=True)