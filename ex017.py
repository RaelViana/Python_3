"""
    Programa que calcula valor de aluguel de carro através do
    preço da diária e do KM rodado.
    Diária > R$60
    Km > R$ 0,15 por km rodado

"""

dias = int(input('Quantos dias alugados ?  ')) # Recebe do usuário valor quantidade de dias
km = float(input('Quantos Km rodados? '))   # recebe valor de km do usuário
pg = (dias * 60) + (km * 0.15)       # faz o calculo de diarias e de km

print('O total a pagar é de R$ {} !'.format(pg)) #print do valor resultante



#--------------------------------------------------------------------------------------------