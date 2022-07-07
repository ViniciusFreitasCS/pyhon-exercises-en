# Calcular a área e quantidade de tinta necessária para pintar uma parede

alt = int(input('\nAltura (m) : '))

larg = int(input('Largura (m) : '))

print('\n=========================================================')
area = alt * larg

tinta = area / 2

print('\nÁrea (m2) : {}'.format(area))

print('\nSão necessários {} litros de tinta para pintar a parede.'.format(tinta))

print('\n=========================================================')
