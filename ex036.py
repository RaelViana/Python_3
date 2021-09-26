

"""
   programa que receba do usuário a distância de uma viagem em Km.
   Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
   e R$0,45 parta viagens mais longas.
"""

distancia = float(input('Qual a distância da viajem: '))
print('Você esta prestes a começar uma viajem de {:.0f}Km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))




#_______________________________________________________________________________