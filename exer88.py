from random import randint
from time import sleep

print('\033[35m-=\033[m'*14)
print('\033[34mPALPITES DE JOGO\033[m'.center(35))
print('\033[35m-=\033[m'*14)

lista = [[],[]]
jogos = int(input('Quantos jogos você quer gerar? '))
print('{:=^35}'.format(f' < SORTEANDO {jogos} JOGOS > '))
for c in range(1,jogos+1):
    for i in range(1,7):
        while True:
            ale = randint(1,60)
            if ale not in lista[0]:
                break
        lista[0].append(ale)
    lista[1].append(lista[0][:])
    lista[0].clear()
for c in lista[1]:
    c.sort()
for c,i in enumerate(lista[1]):
    sleep(1)
    print(f'Jogo{c+1}: ',i)
print(f'{" < Boa Sorte > ":=^35}')

