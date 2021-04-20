print('{:^40}'.format('='*30))
print('{:^40}'.format('ANÁLISE DE DADOS'))
print('{:^40}'.format('='*30))

maiores_18=mulher=homens=0
while True:
    idade = int(input('Qual sua idade? '))
    if idade > 18:
        maiores_18 += 1
    while True:
        sexo = str(input('Qual seu sexo? ')).strip().upper()[0]
        if sexo in 'MF':
            break
        else:
            print('\033[1;31mOPÇÃO INVÁLIDA\033[m')
    if sexo == 'M':
        homens += 1
    else:
        if idade < 20:
            mulher += 1
    while True:
        opcao = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        else:
            print('\033[1;31mOPÇÃO INVÁLIDA\033[m')
    if opcao == 'N':
        break
    else:
        pass
print('-='*17)
print(f'\033[1;37m{maiores_18} pessoas são maiores de 18 anos')
print(f'{homens} Homens foram cadastrados')
print(f'{mulher} Mulheres menores de 20 anos foram cadastradas\033[m')
print('-='*17)

