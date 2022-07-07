# Calcular o aumento salarial de um funcionário

salario = float(input('\nSalário atual (R$) : '))

print('\n===========================')

aumento = salario * 0.15

salario_final = salario + aumento

print('\nAumento (+15%) : {:.2f}'.format(aumento))

print('\nNovo salário (R$) : {:.2f}'.format(salario_final))

print('\n===========================')