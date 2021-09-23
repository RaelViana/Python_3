

"""
   Programa querecebe nome completo de usuario
   * Mostre o nome em letras maiúsculas e minúsculas
   * Quantas letras ao (todo sem considerar espaços)
   * Quantas letras tem o Primeiro Nome

"""
NomeCompleto = str(input('Digite o nome completo: ')).strip()
print('Analisando Seu Nome ...')
print('Seu nome em letras maiúsculas é {} '.format(NomeCompleto.upper()))
print('Seu nome tem letras minúsculas é {} '.format(NomeCompleto.lower()))
print('Seu nome tem ao todo "{}" letras'.format(len(NomeCompleto) - NomeCompleto.count(' ')))
print('O primeiro nome possui "{}" letras'.format(NomeCompleto.find(' ')))




#---------------------------------------------------------------------------------------------