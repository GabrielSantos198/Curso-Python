from time import sleep

# Titulo do Programa
print('\033[34m-=\033[m'*20)
print('\033[32mCONVERSOR DE BASES\033[m'.center(50))
print('\033[34m-=\033[m'*20)

# Programa
num = int(input('Digite um número: '))
print("""
    1- Binário
    2- Octal
    3- Hexadecimal
""")
opcao = int(input('Qual sua escolha de conversão? (1, 2 ou  3) '))
if opcao == 1 or opcao == 2 or opcao == 3:
    print('\033[33mTransformando...\033[m')
    sleep(3)
    if opcao == 1:
        print('O binário de {} é \033[1;32m{}\033[m'.format(num, bin(num)[2:]))
    elif opcao == 2:
        print('O octal de {} é \033[1;35m{}\033[m'.format(num, oct(num)[2:]))
    elif opcao == 3:
        print('O hexadecimal de {} é \033[1;36m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('\033[31mEssa opcão é inexistente\033[m')

