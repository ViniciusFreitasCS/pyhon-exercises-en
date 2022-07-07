# Dissecando uma variável

a = input('Digite algo: ')

print('O tipo do valor {} é {}.'.format(a, type(a)))  # Mostra o tipo da variável

print('Só tem espaços? ', a.isspace())  # Mostra se possui espaços

print('É um número? ', a.isnumeric())  # Mostra se é um número

print('É alfabético? ', a.isalpha())  # Mostra se é alfabético, i.e. só possui letras

print('É alfanumérico? ', a.isalnum())  # Mostra se é alfanumérico

print('Está em maiúsculo?', a.isupper())  # Mostra se tudo está em maiúsculo

print('Está em minúsculo? ', a.islower())  # Mostra se tudo está em minúsculo

print('Está capitalizado? ', a.istitle())  # Mostra se a primeira letra é maiúsculo
