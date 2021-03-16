print('\033[33m=\033[m'*30)
print('\033[1;36;43m{:^30}\033[m'.format('PALINDROMO'))
print('\033[33m=\033[m'*30)

frase = str(input('Digite uma frase: ')).upper().strip().split()
juntar = ''.join(frase)
print(f'\033[1;33mO inverso de {juntar} é {juntar[::-1]}\033[m')
if juntar == juntar[::-1]:
    print('\033[1;32mEssa palavra é um Palindromo\033[m')
else:
    print('\033[1;31mEssa palavra não é um Palindromo\033[m')
