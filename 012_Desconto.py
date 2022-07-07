# Calcular um preço com desconto

valor = int(input('\nPreço (R$) : '))

print('\n=========================================')

desconto = valor * 0.05

valor_final = valor - desconto

print('\nO novo preço com o desconto é de R$ {}'.format(valor_final))

print('\n=========================================')
