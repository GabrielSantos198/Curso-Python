from time import sleep

def frase(txt,ocorrencia):
    if ocorrencia == 1:
        print('\033[42m')
    elif ocorrencia == 2:
        print('\033[44m')
    elif ocorrencia == 3:
        print('\033[41m')
    print('~'*(len(txt)+2))
    print(f' {txt}')
    print('~'*(len(txt)+2))
    print('\033[m')


while True:
    frase('Ajuda Interativa PyHelp',1)
    c = str(input('Função ou Biblioteca> ')).strip()
    frase(f'Acessando o manual do comando "{c}"',2)
    sleep(2)
    help(c)
    while True:
        res = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
        print('\033[31mOpção invalida. Digite Novamente.\033[m')
    if res == 'N':
        break
frase('< PROGRAMA ACABOU >',3)

