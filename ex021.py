from math import radians, sin, cos, tan

"""
   Programa que recebe valor de ângulo qualquer, e exiba seu seno
   cosseno e tangente desse aângulo

"""
Angulo = float(input('digite um valor para o ângulo: '))  # recebe numero real  do usuário

seno = sin(radians(Angulo))  # converte primeiro para radiano e após para seno
print('O Angulo de {:.0f}° tem o seno {:.2f}'.format(Angulo, seno))

cosseno = cos(radians(Angulo))   # converte primeiro para radiano e após para cosseno
print('O Angulo de {:.0f}° tem o cosseno {:.2f}'.format(Angulo, cosseno))


tangente = tan(radians(Angulo)) # converte primeiro para radiano e após para a tangente
print('O Angulo de {:.0f}° tem a tangente de {:.2f}'.format(Angulo, tangente))







# ----------------------------------------------------------------------