

"""
    Programa que lê o comprimento de três retas e
    diga ao usuário se elas podem ou não formar um triângulo.

"""
print('-=' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=' * 20)
reta1 = float(input('Primeiro seguimento: '))
reta2 = float(input('Segundo seguimento: '))
reta3 = float(input('Terceiro seguimento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 +reta3 and reta3 < reta1 + reta2:
    print('Os seguimentos acima "PODEM FORMAR UM TRIÂNGULO"')
else:
    print('Os seguimentos acima "NÃO PODEM FORMAR UM TRIÂNGULO"')






#-----------------------------------------------------------------------------------