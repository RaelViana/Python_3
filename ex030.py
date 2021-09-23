

"""  programa que leia uma frase pelo teclado e mostre:
     * quantas vezes aparece a letra “A”
     * em que posição ela aparece pela primeira vez
     * em que posição ela aparece pela última vez.

     """

frase = str(input('Digite uma frase: ')).upper().strip() 

print('A letra A aparece {} vezes na frase'.format(frase.count('A'))) # Apresenta a ocorrencia de vezes da letra A
print('A preimeira letra A apareceu na posição {}'.format(frase.find('A'))) # Apresenta o indice do primeiro A
print('A útima letra A apareceu na posição {}'.format(frase.rfind('A'))) # Apresenta o indice do utimo A




#--------------------------------------------------------------------------------------------------------------------


