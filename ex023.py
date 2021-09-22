import random  # importa o modulo Random

"""
   Programa que recebe o nome de quatro alunos, e sorteia a ordem 
   de apresetação  dos mesmos.

"""
aluno1 = str(input('Digite o nome do primeiro Aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno:  '))
aluno3 = str(input('digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

lista = [aluno1, aluno2, aluno3,aluno4] # insere os nome em uma lista array

random.shuffle(lista)  # função embaralha randonicamente os itens da lista

print('A ordem de apresentação dos alunos será ')
print(lista)




#___________________________________________________________________________________