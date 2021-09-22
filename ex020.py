import math

"""
   Programa que recebe valor de catetos e calcula a hipotenusa

"""
catetoOposto = float(input('digite um valor para o cateto oposto: '))  # recebe numero real  do usuário
catetoAdjacente = float(input('digite um valor para o cateto adjacente: '))  # recebe numero real  do usuário

hipotenusa = math.hypot(catetoOposto, catetoAdjacente)   # calculo da hipotenusa utilizando método hypot

print(' valor da hipotenusa será de {:.2f}'.format( hipotenusa))

# a função 'math.hypot' efetua o cáulo da hipotenusa


# ----------------------------------------------------------------------