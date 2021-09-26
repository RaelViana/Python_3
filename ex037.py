
from datetime import date  # importação da função date do módulo datetime

"""
   programa que lê  um ano qualquer e mostre se ele é bissexto.

"""
ano = int(input('Que ano deseja Analizar ? '))

if ano == 0:
    ano = date.today().year   # condição retorna ano Atual

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # condição calcula ano bissexto
    print('O ano "{}" é BISSEXTO'.format(ano))
else:
    print('O Ano "{}" não é BISSEXTO'.format(ano))





#-----------------------------------------------------------------------------------