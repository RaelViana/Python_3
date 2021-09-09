"""
    Programa que recebe um número e exiba seu dobro e seu triplo e sua raiz quadrada

"""

n = int(input('Digite um número: '))
d = n*2
t = n*3
rq = n**(1/2) # operação efetua cálculo de raiz quadrada

print('Você digitou: {},  seu dobro é > {} o seu triplo é > {}'.format(n, d, t))
print('a raiz quarada é > {}'.format(rq))