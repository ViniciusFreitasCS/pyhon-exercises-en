# Calcular o preço final de um aluguel de carro

dias = int(input('\nO carro foi alugado por quantos dias? : '))

km = int(input('Quantos quilômetros foram andados? : '))

valor_dia = dias * 60

valor_km = km * 0.15

valor_final = valor_dia + valor_km

print('\n==================NOTA FISCAL====================')

print('\nTempo de uso : R$60,00/dia x {} dias = {:.2f}'.format(dias, valor_dia))

print('\nDistância percorrida : R$0,15/km x {} km = {:.2f}'.format(km, valor_km))

print('\nTotal a pagar : R${:.2f}'.format(valor_final))

print('\n=================================================')