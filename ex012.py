"""
    Programa que recebe valor da carteira e exibe quanto em dolar é possivel comprar .


"""
real =float(input('Qual valor você possui na carteira ? R$ '))
dolar = real / 5.25

print('O valor digitado foi R$ {:.2f} você pode comprar U${:.2f}'.format(real, dolar))



#---------------------------------------