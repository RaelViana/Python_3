"""
    Programa que recebe valor em metros e converte para Unidades de medidas :

    Km - Quilômetros
    hm - Hectômetro
    dam - Decâmetro
    dm - decímetros
    cm - centímetros
    mm - milímetros

"""

medida = float(input('Uma distância em metros: '))

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida de {}m correspode a \n{:.3f}km\n{:.3f}hm\n{:.3f}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))
