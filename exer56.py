print('')
print('\033[33m#\033[m'*30)
print('\033[1;36m{:^30}\033[m'.format('ANALISE DE DADOS'))
print('\033[33m#\033[m'*30)
print('')

media = 0
hmv = 0
cont = 0
hmvn = ' '
for c in range(1,5):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()[0]
    media += idade
    if sexo == 'M' and c == 1:
        hmv = idade
        hmvn = nome
    elif sexo == 'M' and idade > hmv:
        hmv = idade
        hmvn = nome
    elif sexo == 'F' and idade < 20:
        cont += 1
    print('\033[34m-\033[m'*30)

print('\033[1;37m')
print('A média de idade do Grupo foi de {:.0f} Anos'.format(media/4))
print('O homem mais velho do Grupo foi o {} com {} Anos de idade'.format(hmvn, hmv))
print('Têm {} mulheres menores de 20 anos nesse Grupo'.format(cont))
print('\033[m')
