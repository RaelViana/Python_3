

"""
      Estruturas condicionais simples e compostas.


"""

# estrutura simples
nome = str(input('Qual seu nome?  '))

if nome == 'Maria':  # execulta a ação caso valor seja igual
    print('Que lindo nome..')
print('Bom dia "{}" !'.format(nome))


# estrutura composta
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

média = (nota1 + nota2) / 2

print('Sua média foi  {:.1f}'.format(média))

if média >= 6:
    print('Sua média foi boa Parabéns !! ')
else:
    print('Sua média foi ruim ..Estude mais!!')







#############-- FIM --##############
