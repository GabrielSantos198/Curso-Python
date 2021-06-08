from random import randint
from time import sleep
from operator import itemgetter

dado = {}
for c in range(1,5):
    dado[f'jogador{c}'] = randint(1,6)
print('Valores Sorteados: ')
for c,v in dado.items():
    sleep(1)
    print(f'O {c} tirou {v} no dado.')
print('-='*14)
print(f'{"== HANKING DOS JOGADORES ==":>30}')
cont = 0
for c,v in sorted(dado.items(), key=itemgetter(1), reverse=True):
    cont += 1
    print(f'{cont}° lugar: {c} com {v}'.center(30))

