
"""
    Manipulando Texto

"""

 # Fatiamento
frase = 'Curso em Video Python  '

print(frase[9]) # Apresenta a letra no indice 9
print(frase[3:5]) # Apresenta somente o valor fatiado do indice 3 ao 5
print(frase[:14]) # Apresente valor fatiado do inicio até o indice 14
print(frase[9:]) # Apresente valor fatiado do ince 9 até o final
print(frase[0:14:2]) # Aprsenta valor fatiado do inicio até o indice 14, pulando de 2 em  2

dividido = frase.split() # cria uma lista e aloca cada palavra da frase dentro
print(dividido[2]) # apresenta a palavra no indice 2

# Analise

print(frase.count('o')) # Apresenta a recorrência da letra o dentro da frase
print(frase.upper()) # transforma toda a frase um letras maiúsculas
print(frase.lower()) # transforma toda a frase um letras minúsculas
print(len(frase)) # percorre toda a extensão da frase e apresenta a quantidade de caracteres
print(frase.strip()) # remove os espaços antes e depois da frase
print(frase.replace('Python', 'Android')) # Substitui a palavra da frase, pela palavra referenciada
print('Curso' in frase) # Verifica se existe a palavra referenciada dentro da frase
print(frase.find('Video')) # Retorna o indice de onde a palavra está alocada
print(frase.capitalize()) # Torna a primeira letra da frase Maiúscula e o restante Minúscula
print(frase.title()) # Torna todas as palavras iniciando com letras Maiúsculas
print('-'.join(frase)) # insere um caracter especifico entre os espaçõs de cada letra




#--------------------------------------------------------------------------------------------------------