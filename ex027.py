


"""
   Programa lê um número de  0 a 9999 e
   mostre na tela cada um dos seus digitos separados

"""

numero = int(input('Digite um número: ')) #recebe numero do usuário

unidade = numero // 1 % 10   # converte numero digitado para unidade
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10


print('Analisando o número digitado ..')
print('A unidade = {} '.format(unidade))
print('A dezena = {}'.format(dezena))
print('A centena = {}'.format(centena))
print('A milhar = {}'.format(milhar))




#------------------------------------------------------------------------------------------



