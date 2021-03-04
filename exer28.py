from random import randint
from time import sleep

computador = randint(0,5)
print('\033[33m-=\033[m'*28)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[33m-=\033[m'*28)
jogador = int(input('Em que número eu pensei? '))
print('\033[35mPROCESSANDO...\033[m')
sleep(2)
if computador == jogador:
    print('\033[32mParabéns você acertou!\033[m')
else:
    print('\033[31mSinto muito você errou, eu pensei no número {}!\033[m '.format(computador))

