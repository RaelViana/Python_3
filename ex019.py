from math import trunc  # importação apenas o metodo trunc da biblioteca math

"""
   Programa que recebe um numero real qualquer digitado pelo usuário e mostre
   sua porção inteira

"""
numeroReal = float(input('digite um número real: '))  # recebe numero real  do usuário

print('O número digitado foi {} a sua porção inteira é {}'.format(numeroReal, trunc(numeroReal)))

# a função 'trunc' corta a parte iteira no número


# ---------------------------------------------------------------------------