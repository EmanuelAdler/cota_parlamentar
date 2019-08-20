# -*- coding: utf-8 -*-
import pandas as pd
def mergeFiles(startYear, endYear):
    for year in range(startYear, endYear+1):
        filename = 'eventosPresencaDeputados-' + str(year) + '.csv'
        print(filename)
        if(year == startYear):
            df = pd.read_csv(filename, sep=';')
        else:
            buff = pd.read_csv(filename, sep=';')
            df = df.append(buff)
    return df

yearsRange = [2015, 2018] 
df = mergeFiles(yearsRange[0], yearsRange[1])
filename = "eventos" + str(yearsRange[0]) + '-' + str(yearsRange[1]) + '.csv'
df.to_csv(filename, encoding = 'utf-8', index = True)
newdf = pd.read_csv(filename)



