from random import randint
from time import sleep

# Título do Programa
print()
print('\033[33m-=\033[m'*28)
print('{:^40}'.format('\033[34mVou pensar em um número entre 0 e 10. Tente Adivinhar...\033[m'))
print('\033[33m-=\033[m'*28)
print()

# Código do Programa
cont = 0
maquina = randint(0,10)
humano = int(input('Digite um número: '))
while maquina != humano:
    cont += 1
    if humano < maquina:
        print('Mais')
    else:
        print('Menos')
    humano = int(input('Digite um número: '))
print()
print('-'*35)
print('\033[1;32mParabéns você acertou eu pensei no {}\033[m'.format(maquina))
if cont == 0:
    print('\033[1mVocê acertou de Primeira.\033[m')
else:
    print('\033[1mVocê acertou com {} tentativas'.format(cont))
print('-'*35)
