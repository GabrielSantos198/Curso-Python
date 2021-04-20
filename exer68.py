from random import randint

# Titulo do Programa
print()
print('\033[33m{}\033[m'.format('=-='*10))
print('\033[34m{}\033[m'.format('VAMOS JOGAR PAR ou IMPAR'))
print('\033[33m{}\033[m'.format('=-='*10))
print()

cont= 0
while True:
    maquina = randint(0,10)
    humano = int(input('Digite um número: '))
    opcao = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    while opcao not in 'PI':
        print('\033[1;31mPor favor digite uma opção válida\033[m')
        opcao = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    s = humano + maquina
    if s%2 == 0 and opcao == 'P':
        cont += 1
        print('-'*40)
        print(f'Você jogou {humano} e a maquina jogou {maquina}. Deu PAR')
        print('-'*40)
        print('\033[1;32mVocê Venceu!\033[m')
        print('Vamos jogar novamente ...')
        print('~'*40)
    elif s%2 == 1 and opcao == 'I':
        cont += 1
        print('-'*40)
        print(f'Você jogou {humano} e a maquina jogou {maquina}. Deu IMPAR')
        print('-'*40)
        print('\033[1;32mVocê Venceu!\033[m')
        print('Vamos jogar novamente ...')
        print('~'*40)
    else:
        print('-'*40)
        if s%2 == 0:
            print(f'Você jogou {humano} e a maquina jogou {maquina}. Deu PAR')
        else:
            print(f'Você jogou {humano} e a maquina jogou {maquina}. Deu IMPAR')
        print('Game Over.', end="")
        print('Você venceu {} vezes'.format(cont))
        print('-'*40)
        break

