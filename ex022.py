import random  # importa o modulo Random

"""
   Programa que recebe o nome de Quatro alunos, e escolhe um
   aleatóriamente peo sistema

"""
aluno1 = str(input('Digite o nome do primeiro Aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno:  '))
aluno3 = str(input('digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

lista = [aluno1, aluno2, aluno3,aluno4] # insere os nome em uma lista array

escolhido = random.choice(lista) # função escolhe randonicamente um item da lista

print('O Aluno escolhido foi   "{}"'.format(escolhido)) #print do nome escolhido




#___________________________________________________________________________________