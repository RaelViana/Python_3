"""
    Programa que efetua o cálculo de uma área e indica quantos litros e tinta é necessário
    para aplicação

"""
lar = float(input('Largura da parede: '))
alt = float(input('Altura da parde: '))
area = lar * alt   #função efetua cáulculo de área

print('Sua pade tem a dimensão de {}x{}  e sua área é de {}m²'.format(lar, alt, area))

tinta= area / 2

print('Para pintar sua parede, você precisará de {}l de tinta'.format(tinta))