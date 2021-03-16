print('\033[34m-=\033[m'*25)
print('\033[1;35mCONDIÇÃO PARA A EXISTÊNCIA DE UM TRIÂNGULO\033[m')
print('\033[34m-=\033[m'*25)

l1 = float(input('Primeira medida: '))
l2 = float(input('Segunda medida: '))
l3 = float(input('Terceira medida: '))
menor = min(l1, l2, l3)
maior = max(l1, l2, l3)
meio = (l1+l2+l3) - (menor+maior)
if menor+meio > maior:
    print('\033[1;32mCom esses complimentos de retas é possível formar um triângulo. ', end='')
    if l1 == l2 and l1 == l3:
        print('Como todos os lados do triângulo são iguais o tipo do triângulo que será formado será um Equilátero')
    elif l1 == l2 or l1 == l3  or l2 == l3:
        print('Como só dois lados do triângulo são iguais o tipo do triângulo que será formado será um Isósceles')
    else:
        print('Como tods os lados do triângulo são diferentes o triângulo que será formado será um Escaleno')
    print('\033[m')
else:
    print('\033[1;31mCom esses complimentos de retas não é possível formar um triângulo\033[m')

