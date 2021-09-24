

"""
     programa que leia o nome completo de uma pessoa, mostrando
      em seguida o primeiro e o último nome separadamente.

 """
nome = str(input('Digite seu nome completo: ')).strip()

listaNome = nome.split()  # recebe o nome completo e divide em uma lista

print('Olá "{}" é um prazer te conhecer !!'.format(nome))

print('Seu primerio nome é > {}'.format(listaNome[0])) # Exibe o Primeiro indice da lista

print('O seu útimo nome é > {}'.format(listaNome[len(listaNome)-1])) # Percorre toda lista e retorna o último



#______________________________________________________________________________________________________________
