cont = 0
dic1 = {}
lista = []

while True:
    cont += 1
    dic1['nome'] = str(input(f'Digite o nome da {cont}ª pessoa: ')).strip()
    while True:
        sexo = str(input('Digite o sexo dela: [M/F] ')).strip().upper()[0]
        if sexo in 'FM':
            break
        print('\033[1;31mOpção inexistente...Por favor digite uma opção valida!\033[m')
    dic1['sexo'] = sexo
    dic1['idade'] = int(input('Digite a idade dessa pessoa: '))
    lista.append(dic1.copy())
    dic1.clear()
    while True:
        res = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
        print('\033[1;31mOpção inexistente...Por favor digite uma opção valida!\033[m')
    if res == 'N':
        break
print('-='*16)
print(f'Foram cadastrados {len(lista)} pessoas')
media = 0
for c,v in enumerate(lista):
    media += v['idade']
print(f'A media de idade do grupo é {media/len(lista):.0f} anos')
mulheres = []
acima = []
for c in lista:
    if c['sexo'] == 'F':
        mulheres.append(c['nome'])
if len(mulheres) != 0:
    print(f'Mulheres cadastradas: {mulheres}')
else:
    print('Nem uma mulher foi cadastrada')
for c in lista:
    if c['idade'] > media/len(lista):
        acima.append(c['nome'])
if len(acima) != 0:
    print(f'Pessoas com idade acima da media: {acima}')
else:
    print('Nem uma pessoa ficou com idade acima da media')


