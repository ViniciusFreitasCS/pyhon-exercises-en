# Calcular o aumento salarial de um funcionário

salario = float(input('\nSalário atual (R$) : '))

print('\n===========================')

aumento = salario * 0.15

salario_final = salario + aumento

print(f'\nAumento (+15%) : {aumento:.2f}')

print(f'\nNovo salário (R$) : {salario_final:.2f}')

print('\n===========================')
