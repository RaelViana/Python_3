"""
    Programa que efetua o cálculo de desconto de um produto

"""

preco = float(input('Qual é o valor do produto? R$ '))
atual = preco - (preco * 5 / 100)

print('Preço do produto R$ {:.2f}, valor com desconto de 5% é de R$ {:.2f}'.format(preco, atual))




#______________________________________________