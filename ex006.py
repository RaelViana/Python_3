"""
    Operadores Aritméticos-
    + Adição
    - subtração
    * multiplicação
    / divisão
    ** potência
    // divisão inteira
    % resto da divisão

    Ordem de precedência -
    1° () - parenteses
    2° ** - exponenciação
    3° * / // % - um dos quatro operadores
    4° +  -   adição ou subtração

"""
  # Exemplos

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
rd = n1 % n2

print('A Soma é = {},\n o subtração é = {},\n e o produto é = {}'.format(a,s, m))
print('A divisão é = {},\n a divisão inteira é = {},\n e a exponenciação é  = {:.3f} '.format(d, di, e))
print('o resto da divisão é  = {}'.format(rd))

# obs(\n) efutua quebra de linha , (:.3f) formata o valor com 3 casas flutuantes decimais 



 # Exemplo ordem de precedência-

x = 4 - 3 +(2+2) * 5 /2
y = 5 * 3 - 2 + 2**3

print('O resultado de x é = {}'.format(x))
print('O resultado de y é = {}'.format(y))
