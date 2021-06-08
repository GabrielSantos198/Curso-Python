from time import sleep

print('-='*14)
print('ANALISE DE DADOS'.center(28))
print('-='*14)

pessoas = [[],[]]
while True:
    pessoas[0].append(str(input('Digite seu nome: ')))
    pessoas[1].append(float(input('Digite seu peso: ')))
    while True:
        res = str(input('Você quer continua? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
        print('\033[31mOpção Invalida...Digite novamente.\033[m')
    if res == 'N':
        break

print('-='*14)
print('\033[35mAnalisando...\033[m'.center(38))
print('-='*14)
sleep(3)

print(f'>>> Foram cadastradas {len(pessoas[0])} pessoas')
print('>>> As pessoas mais pesadas digitadas foram: ', end='')
maior = max(pessoas[1])
tot0 = pessoas[1].count(maior)
calc0 = 1
for c, e in enumerate(pessoas[1]):
    if e == max(pessoas[1]):
        if calc0 < tot0:
            print(pessoas[0][c], end=', ')
        else:
            print(pessoas[0][c])
        calc0 += 1
print('>>> As pessoas mais leves digitadas foram: ', end='')
menor = min(pessoas[1])
tot = pessoas[1].count(menor)
calc = 1
for c, e in enumerate(pessoas[1]):
    if e == min(pessoas[1]):
        if calc < tot:
            print(pessoas[0][c], end=', ')
        else:
            print(pessoas[0][c])
        calc += 1

