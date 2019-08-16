# -*- coding: utf-8 -*-
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

df = pd.read_csv('2015-2019.csv')
df = df.drop(columns=['nuCarteiraParlamentar', 'codLegislatura', 'txtFornecedor', 
                      'txtCNPJCPF', 'nuCarteiraParlamentar', 'indTipoDocumento', 
                      'vlrDocumento', 'vlrGlosa', 'numParcela', 'txtTrecho', 'numLote'])
df = df.sort_values(['vlrLiquido'], ascending=False)
topSpenders = df.head(30)