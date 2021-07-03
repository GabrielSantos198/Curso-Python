print('\033[35m-=\033[m'*14)
print('\033[1;34mFACTORIAL\033[m'.center(38))
print('\033[35m-=\033[m'*14)

def fatorial(num,show=False):
    """
    Calcule o fatorial de um número:
    num: Número a ser calculado
    show: Parâmetro opcional que mostra ou não o processo de fatoramento
    autor: GabrielSantos198
    """
    calc = 1
    for c in range(num,0,-1):
        calc *= c
        if show == True:
            if c > 1:
                print(c,end=' x ')
            else:
                print(f'1 = {calc}')
    if show == False:
        print(calc)


fatorial(5)

