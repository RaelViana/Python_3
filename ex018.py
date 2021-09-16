import math         #importação da biblioteca math

"""
    Aplicação do Módulo  Math
    
"""
num = int(input('digite um número par a raiz Quadrada: ')) #recebe num do usuário
rq = math.sqrt(num)   #aplica a função square root(raiz quadrada) em num

print('A raiz quadrada de {} é {}'.format(num, math.ceil(rq)))

# a função '.ceil' arredonda para cima um valor real




#---------------------------------------------------------------------------