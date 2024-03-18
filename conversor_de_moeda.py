# 1 dolar = 4,96 real
# 1 iene japa = 0,033 real
# 1 euro = 5,37 real

grana = float(input('Sua grana: '))

conversor_dolar = grana / 4.96

conversor_iene = grana / 0.033

conversor_euro = grana / 5.37

print('com {} reais vc consegue comprar {} dolars' .format(grana, conversor_dolar))

print('/n')

print('com {} reais vc consegue comprar {} ienes' .format(grana, conversor_iene))

print('/n')

print('com {} reais vc consegue comprar {} euros'.format(grana, conversor_euro))

