def leiaDinheiro(num):
    while True:
        n = input(num).replace(',','.')
        if n.replace('.','').isnumeric():
            break
        print('\033[31mErro digite um número valido\033[m')
    return float(n)

