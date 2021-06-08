print('\033[34m-=\033[m'*20)
print('\033[32m{:^35}\033[m'.format('TABELA'))
print('\033[34m-=\033[m'*20)
print()

produtos = ('Lapiseira', 1, 'Celular', 1000, 'Notebook', 1500, 'Caderno', 30, 'Geladeira', 3000)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='')
    else:
        print(f'  R$ {produtos[c]:>4}')
print()
print('\033[34m-=\033[m'*20)
