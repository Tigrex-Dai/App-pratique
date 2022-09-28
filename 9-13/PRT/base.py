# -*- coding: utf-8 -*-

import pandas as pd
import os
from pathlib import Path
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# df = pd.read_excel('./resultat-prts-2014.xls')
dflist = []

path = Path(Path.cwd())
tempdf = pd.DataFrame()
for i in path.glob("*.xls*"):
  test = pd.read_excel(i, sheet_name=None)
  keys = list(test.keys())
  #print(keys)
  for g in keys:
      temp = test[g]
      tempdf = pd.concat([temp, pd.DataFrame(columns=['fname', 'type', 'year'])])
      tempdf.loc[:, 'fname'] = Path(i).stem.split('.')[0]
      dflist.append(tempdf)
# print(type(temp.loc[:, 'fname'][0]))
# print(type(dflist[0].loc[:, 'year'][0]))
final = pd.DataFrame()
for h in dflist:
  #print(h.loc[:, 'fname'][0])
  if h.loc[:, 'fname'][0].startswith('prt'):
    #print(h.loc[:, 'fname'][0].startswith('prt'))
    if h.loc[:, 'fname'][0].startswith('prt-k'):
      h.loc[:, 'type'] = 'PRT-K'
      h.loc[:, 'year'] = '2020'
    else:
      h.loc[:, 'type'] = 'PRT-S'
      if h.loc[:, 'fname'][0].startswith('prts_20'):
        h.loc[:, 'year'] = '2020'
      else:
        h.loc[:, 'year'] = '2021'
  else:
    for j in range(2012, 2020):
      #print(h.loc[:, 'fname'][0].find(str(j)))
      if h.loc[:, 'fname'][0].find(str(j)) != -1:
        h.loc[:, 'year'] = str(j)
        #print('j:', j)
    if h.loc[:, 'fname'][0].find('prts')+h.loc[:, 'fname'][0].find('prt-s')!=-2:
      h.loc[:, 'type'] = 'PRT-S'
    else:
      h.loc[:, 'type'] = 'PRT-K'
  #print(h.loc[:, 'type'][0])
  for k in h.columns.tolist():
      #print(type(k))
      if k.find('Montant')+k.find('montant')+k.find('Autorisation')+k.find('autorisation')!=-4:
          h.rename(columns={k:'Montant'}, inplace=True)
  #h = h[~np.isnan(h).any(axis=1)]
  if h.loc[:, 'year'][0] == '2021' and h.loc[:, 'type'][0] == 'PRT-S':
      #print(h)
      h.drop([13,14,15],inplace=True)
      #print(h.loc[10,'Montant'])
      h.loc[10, 'Montant'] = 838426
      h.loc[11, 'Montant'] = 324700
      h.loc[12, 'Montant'] = 224389

#print(dflist[0].columns)
  # print(h.columns)
  final = pd.concat([final,h[['year','type','Montant']]])
  final['year'] = final['year'].astype('int')
final.to_csv('./PRT.csv')

final2 = final.groupby(by='year').agg({'Montant':'sum'})
final2.plot(
    marker="o",
    linestyle="dashed",
    title=" Montant Accordé entre 2012 et 2020",
    figsize=(8, 6),
    fontsize=16,
    xlim=(2013, 2021)
)