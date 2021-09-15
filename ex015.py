"""
    Programa que efetua o cálculo de reajuste salarial

"""

salario = float(input('Qual é o salário do funcionário? R$ '))
novo = salario + (salario * 15 / 100)

print('O Salário que recebia R$ {:.2f}, com aumento de 15% passa a receber R$ {:.2f}'.format(salario, novo))




#______________________________________________