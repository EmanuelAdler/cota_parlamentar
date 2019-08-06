import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

df = pd.read_csv('Gastos-Quota-Parlamentar.csv', dtype={'reimbursement_numbers': object}, nrows=10)

print(df)
