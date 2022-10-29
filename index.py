import pandas as pd
import os

pasta = './planilhas'

for _, _, arquivo in os.walk(pasta):
    nomesDosArquivos = arquivo

linhasPlanilha = list()

for arquivo in nomesDosArquivos:
    path = pasta+'/'+arquivo
    linhasPlanilha.append(pd.read_excel(path))

planilha = pd.concat(linhasPlanilha)
planilha.to_excel('planilha_completa.xlsx', index=False)
print(planilha)