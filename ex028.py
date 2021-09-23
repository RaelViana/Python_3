

"""
   Programa lê o nome de uma cidade e verifica se ela
   começa com 'Santo' ou não

"""
cidade = str(input('Informe a cidade : ')).strip()  # .strip elimina os esaços da frase recebida

print(cidade[:5].upper() == 'SANTO') # [:5]percorre os 5 itens e verifica se é verdadeiro ou falso


#-------------------------------------------------------------------------------------------------------