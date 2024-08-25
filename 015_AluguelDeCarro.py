# Calcular o preço final de um aluguel de carro

dias = int(input('\nO carro foi alugado por quantos dias? : '))

km = int(input('Quantos quilômetros foram andados? : '))

valor_dia = dias * 60

valor_km = km * 0.15

valor_final = valor_dia + valor_km

print('\n==================NOTA FISCAL====================')

print(f'\nTempo de uso : R$60,00/dia x {dias} dias = {valor_dia:.2f}')

print(f'\nDistância percorrida : R$0,15/km x {km} km = {valor_km:.2f}')

print(f'\nTotal a pagar : R${valor_final:.2f}')

print('\n=================================================')
