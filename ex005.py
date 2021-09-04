"""
    Dissecando uma Variável
"""

a = input('Digite algo > ') # recebe variavel de qualquer tipo digitada pelo usuário

print('O tipo primitivo desse valor é ', type(a)) # apresenta o tipo da variável
print('Só tem espaços ?', a.isspace())        # verifica se foi digitado somente espaços
print('É um Número ?', a.isnumeric())         # verifica se o valor é numérico
print('É alfabético ?', a.isalpha())          # verifica se o valor é alfabetico
print('É alfanumérico ?', a.isalnum())        # verifica se o valor é alfanumérico
print('Está em Maiúsculas ?', a.isupper())    # verifica se o valor esta em letra Maiúsculas
print('Está em Minúsculas ?', a.islower())    # verifica se o valor esta em letra Minúsculas
print('Está Captalizada ?', a.istitle())      # verifica se o valor esta com a primeira letra Maiúscula
