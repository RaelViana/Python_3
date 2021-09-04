""" Tipos primitivos e Saída de Dados:

     int - para números inteiros.
     str - (string) textos, palavras.
     float - para números reais, quebrados, fracionados.
     bool - (boolean) lógicos- verdadeiros ou falsos

  """

# int()----------------------------------------
n1 = int(input('Digite o primeiro número: '))  # recebe um valor inteiro digitado pelo usuário
n2 = int(input('Digite o segundo número: '))  # recebe outro valor inteiro digitado pelo usuário
soma = n1 + n2  # variável soma, efetua a operação entre n1 e n2
print('A soma ente', n1 , ' e ', n2 , ' é = ', soma) # imprime a msg e o resultado da variavel soma
print('A soma entre {} e {} = {}'.format(n1, n2, soma)) # imprime utilizando outro método
print(type(n1)) # imprime o valor e o tipo primitivo


# str()----------------------------------------
s = input('Digite seu Nome: ')  # recebe valor de uma string digitada pelo usuário
print('Seja bem vindo, {} !'.format(s)) # imprime msg e valor da str

# float()--------------------------------------
f1 =float(34.5) # recebe um número real
f2 = float(2.74) # recebe um número real
sf = f1 / f2     # efetua uma operação de divisão entre as variáveis
print('A divisão entre {} e {} = {}'.format(f1, f2, sf)) # Imprime o valor da operação


# bool()----------------------------------------
a = 'São Paulo'   # recebe um valor string
b = 467
x = bool(a)  # verifica valor boolean em a

print('A variável - a, {} é uma string ? {}'.format(a, x))
print(a.isnumeric())  # verifica se o valor de 'a' é numerico
print(a.isalpha())  # verifica  se o valor é em letras
print(a.isalnum())  # verifica se o valor de 'a' é alphanumerico
