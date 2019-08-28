#4- Qual partido gasta mais, proporcionalmente?
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # plot graphs
import seaborn as sns # beautify graphs

#df = pd.read_csv('Gastos-Quota-Parlamentar.csv', dtype={'reimbursement_numbers': object})
df = pd.read_csv('2015-2019.csv')
#Dropping unnecessary columns
#df = df.drop(columns=['congressperson_document', 'term_id', 'supplier', 'cnpj_cpf', 'document_number', 'document_type', 'document_value', 'remark_value', 'installment', 'passenger', 'leg_of_the_trip', 'batch_number'])
df = df.drop(columns=['nuCarteiraParlamentar', 'codLegislatura', 'txtFornecedor', 
                      'txtCNPJCPF', 'nuCarteiraParlamentar', 'indTipoDocumento', 
                      'vlrDocumento', 'vlrGlosa', 'numParcela', 'txtTrecho', 'numLote'])
list(df.columns)
#Selecting years we will use
years = [2015, 2016, 2017, 2018]
#Filtering dataset with years
df1 = df[df.numAno.isin(years)]

partySpendings = df1.groupby(['sgPartido'])['vlrLiquido'].sum().to_frame(name = 'valorGasto').reset_index()
congressPersonTotal = df1.groupby(['sgPartido'])['ideCadastro'].nunique()

# usando o to_frame() pois o metodo merge exige que seja um dataframe e nao uma serie
df2 = pd.merge(partySpendings, congressPersonTotal.to_frame(), on='sgPartido')
df2.reset_index()

#df2['avg'] = df2[['net_values', 'congressperson_id']].mean(axis=1)
df2['avg'] = df2['valorGasto']/df2['ideCadastro']

df2 = df2.sort_values(['avg'], ascending=False)
#df2.plot.bar(y = 'avg', legend=False)
sns.barplot(x=df2.avg, y=df2.sgPartido, data=df2).set(ylabel='Sigla do Partido', xlabel='Média de gasto por deputado')

print (df2)

plt.show()