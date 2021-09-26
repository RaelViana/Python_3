

"""
   programa que lê três números e mostre qual é o maior e qual é o menor.

"""
A = int(input('Digite o primeiro número: '))
B = int(input('Digite o segundo número: '))
C = int(input('Digite o terceiro número: '))

# verificando Qual é o menor
menor= A
if B < A and B < C:
    menor = B
if C < A and C < B:
    menor = C

print('O menor número digitado foi "{}"'.format(menor))

# Verificando Qual é o Maior
maior = A
if B > A and B > C:
    maior = B
if C >A and C > B:
    maior = C

print('O Maior número digitado foi "{}"'.format(maior))




#-----------------------------------------------------------------------------------