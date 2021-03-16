from random import choice
from time import sleep

print('')
print('\033[34m=\033[m'*35)
print('{:^45}'.format('\033[1;36mJOKÊNPÔ\033[m'))
print('\033[34m=\033[m'*35)
print('')

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
maquina = choice(opcoes)
humano = str(input('Você escolhe PEDRA, PAPEL ou TESOURA? ')).strip().upper()
if humano == 'PEDRA' or humano == 'PAPEL' or humano == 'TESOURA':
    print('\033[1;33mJO\033[m')
    sleep(1)
    print('\033[1;31mKÊN\033[m')
    sleep(1)
    print('\033[1;36mPÔ\033[m')

    if maquina == humano:
        print('Empate')
    elif maquina == 'PEDRA' and humano == 'TESOURA':
        print('\033[1;31mA maquina escolheu Pedra. Você Perdeu!\033[m')
    elif maquina == 'PEDRA' and humano == 'PAPEL':
        print('\033[1;32mA maquina escolheu Pedra. Parabéns você Venceu\033[m')
    elif maquina == 'PAPEL' and humano == 'PEDRA':
        print('\033[1;31mA maquina escolheu Papel. Você Perdeu!\033[m')
    elif maquina == 'PAPEL' and humano == 'TESOURA':
        print('\033[1;32mA maquina escolheu Papel. Parabéns você Venceu!\033[m')
    elif maquina == 'TESOURA' and humano == 'PEDRA':
        print('\033[1;32mA maquina escolheu Tesoura. Parabéns você Venceu\033[m')
    elif maquina == 'TESOURA' and humano == 'PAPEL':
        print('\033[1;31mA maquina escolheu Tesoura. Você Perdeu!\033[m')
else:
    print('\033[1;31mEssa opção é inesistente.\033[m')

