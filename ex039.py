


"""
   programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
   Para salários superiores a R$1250,00, calcule um aumento de 10%.
   Para os inferiores ou iguais, o aumento é de 15%.

"""

salario = float(input('Qual é o salario do fincionário? R$ '))

if salario <= 1250:
    novoSalario = salario + (salario * 15 / 100)
else:
    novoSalario = salario + (salario * 10 / 100)

print('Quem ganhava R$ {:.0f} passará a ganhar R${:.0f}'.format(salario, novoSalario))






#-----------------------------------------------------------------------------------