from random import randint               # importa a função randint
from time import sleep                   # Importa a função time
"""
    Programa que faz o computador “pensar” em um número inteiro entre 0 e 5
    e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

"""

computador = randint(0, 5) #comando faz computador sortear numero randonicamente

print('-=-' * 20)
print('Vou pensar em um numero de  0 a 5. Tente adivinhar... ')
print('-=-' * 20)

jogador = int(input('Digite seu palpite: ')) # usuario tenta adivinhar o número
print('PROCESSANDO...')
sleep(3)    # função faz com que a ação demore 3 segundos para ser executada

if jogador == computador:
    print('Parabéns você acertou o palpite !!!')
else:
    print('O numero foi "{}" Que pena você errou !!! '.format(computador))






#_________________________________FIM________________________________________________