

"""
   programa que lê um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

"""
numero = int(input('Digite um numero: '))

resultado = numero % 2

if resultado == 0:
    print('O numero digitado foi {} ele é um número "par"'.format(numero))
else:
    print('O numero digitado foi {} ele é um número "impar"'.format(numero))






#__________________________________________________________________________
