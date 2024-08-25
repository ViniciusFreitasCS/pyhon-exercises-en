# Calcular a área e quantidade de tinta necessária para pintar uma parede

alt = int(input('\nAltura (m) : '))

larg = int(input('Largura (m) : '))

print('\n=========================================================')
area = alt * larg

tinta = area / 2

print(f'\nÁrea (m2) : {area}')

print(f'\nSão necessários {tinta} litros de tinta para pintar a parede.')

print('\n=========================================================')
