sexo = str(input('Qual seu sexo? ')).strip().upper()[0]
while sexo not in 'MmFf':
    print('\033[1;31mInvalido\033[m')
    sexo = str(input('Qual seu sexo? ')).strip().upper()[0]
print('Acabou')

