# Título do Programa
print('\033[34m-=\033[m'*15)
print('{:^40}'.format('\033[1;35mTABÚADA\033[m'))
print('\033[34m-=\033[m'*15)

while True:
    num = int(input('Digite um número: \033[1;37mNúmeros negativos param o Programa \033[m'))
    if num < 0:
        break
    s = 0
    while s < 9:
        s += 1
        print(f'{num} X {s} = {num*s}'.center(40))
    print()
print('\033[1;37mFim\033[m')   
